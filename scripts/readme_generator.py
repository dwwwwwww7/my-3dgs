import json
import datetime
import sys
from linecache import updatecache
from pathlib import Path
import re
import argparse
import requests
import time
import random
import uuid
import urllib3
import os

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class EdgeTranslator:
    """使用Edge浏览器翻译API的翻译器"""

    def __init__(self, max_retries: int = 3, delay: float = 1.0):
        self.max_retries = max_retries
        self.delay = delay
        self.user_agent = self._generate_user_agent()
        self.translation_api = "https://api-edge.cognitive.microsofttranslator.com/translate"

    def _generate_user_agent(self) -> str:
        """生成随机User-Agent模拟浏览器"""
        browsers = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 EdgA/114.0.1823.43"
        ]
        return random.choice(browsers)

    def _get_edge_token(self) -> str:
        """获取Edge翻译API的授权令牌"""
        auth_url = "https://edge.microsoft.com/translate/auth"
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.microsoft.com/",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site"
        }

        for attempt in range(self.max_retries):
            try:
                response = requests.get(auth_url, headers=headers, timeout=10, verify=False)
                response.raise_for_status()
                return response.text
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay * (2 ** attempt))
                else:
                    raise RuntimeError(f"获取Edge令牌失败: {str(e)}")

    def _send_preflight(self, token: str):
        """发送预检请求（OPTIONS）准备翻译"""
        params = {
            "from": "en",
            "to": "zh-CHS",
            "api-version": "3.0",
            "includeSentenceLength": "true"
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": self.user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.microsoft.com/",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Origin": "https://www.microsoft.com"
        }

        try:
            requests.options(
                self.translation_api,
                params=params,
                headers=headers,
                timeout=10,
                verify=False
            )
        except Exception:
            # 预检请求失败不影响后续翻译
            pass

    def translate_abstract(self, abstract: str) -> str:
        """翻译论文摘要（英->中）"""
        if not abstract.strip():
            return ""

        # 处理超长摘要（API限制约5000字符）
        if len(abstract) > 4500:
            abstract = abstract[:4500] + "..."

        # 生成请求ID和会话ID
        trace_id = str(uuid.uuid4())
        session_id = str(uuid.uuid4())

        # 获取授权令牌
        token = self._get_edge_token()

        # 发送预检请求
        self._send_preflight(token)

        # 准备翻译请求
        params = {
            "from": "en",
            "to": "zh-CHS",
            "api-version": "3.0",
            "includeSentenceLength": "true"
        }

        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": self.user_agent,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.microsoft.com/",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Origin": "https://www.microsoft.com",
            "X-ClientTraceId": trace_id
        }

        body = [{"Text": abstract}]

        # 尝试翻译（含指数退避重试）
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.translation_api,
                    params=params,
                    headers=headers,
                    json=body,
                    timeout=15,
                    verify=False
                )
                response.raise_for_status()

                # 解析翻译结果
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    translations = result[0].get("translations", [])
                    if translations:
                        return translations[0].get("text", "")

                return abstract  # 翻译失败时返回原文

            except Exception as e:
                if attempt < self.max_retries - 1:
                    # 指数退避等待
                    time.sleep(self.delay * (2 ** attempt))
                else:
                    return f"[翻译失败] {str(e)}"


def load_latest_papers(data_dir: Path) -> list:
    """加载最新的论文数据"""
    json_files = list(data_dir.glob("papers_*.json"))
    if not json_files:
        print("未找到论文数据文件")
        return []

    latest_file = max(json_files, key=lambda x: x.stat().st_mtime)
    print(f"找到最新数据文件: {latest_file}")

    with open(latest_file, "r", encoding="utf-8") as f:
        papers = json.load(f)
        print(f"成功从{latest_file}加载{len(papers)}篇论文")
        return papers


def translate_papers_abstracts(papers: list, translator: EdgeTranslator) -> list:
    """翻译所有论文的摘要"""
    if not translator:
        print("翻译器未初始化，跳过摘要翻译")
        return papers

    print("开始翻译论文摘要...")
    translated_papers = []

    for i, paper in enumerate(papers):
        try:
            # 复制论文数据
            translated_paper = paper.copy()

            # 翻译摘要
            abstract_en = paper.get("abstract", "")
            if abstract_en:
                abstract_zh = translator.translate_abstract(abstract_en)
                translated_paper["abstract_zh"] = abstract_zh

                # 添加翻译状态标记
                if "[翻译失败]" in abstract_zh or "[翻译错误]" in abstract_zh:
                    print(f"论文 {i + 1}/{len(papers)} 翻译失败: {abstract_zh}")
                else:
                    print(f"论文 {i + 1}/{len(papers)} 翻译成功")
            else:
                translated_paper["abstract_zh"] = ""
                print(f"论文 {i + 1}/{len(papers)} 无摘要可翻译")

            translated_papers.append(translated_paper)

            # 添加延迟避免触发API限制
            if i < len(papers) - 1:
                time.sleep(1.0)  # 每篇论文之间延迟1秒

        except Exception as e:
            print(f"翻译论文 {i + 1}/{len(papers)} 时出错: {str(e)}")
            translated_paper["abstract_zh"] = f"[翻译错误] {str(e)}"
            translated_papers.append(translated_paper)

    print("摘要翻译完成")
    return translated_papers

def group_papers_by_month(papers: list) -> dict:
    """按月份分组论文"""
    papers_by_month = {}
    for paper in papers:
        try:
            date = datetime.datetime.strptime(paper["published_date"], "%Y-%m-%d")
            month_key = date.strftime("%B %Y")  # 格式: "August 2025"
            if month_key not in papers_by_month:
                papers_by_month[month_key] = []
            papers_by_month[month_key].append(paper)
        except Exception:
            # 跳过日期格式无效的论文
            continue
    return papers_by_month


def format_paper_entry(paper: dict, index: int) -> str:
    """格式化单篇论文信息"""
    try:
        arxiv_id = paper["arxiv_url"].split("/")[-1]

        # 清理标题中的换行符和多余空格
        title = paper['title'].replace('\n', ' ').replace('  ', ' ').strip()

        # 序号和标题
        entry = f"### [{index}] {title}  \n"

        # 发布时间
        pub_date = paper["published_date"]
        update_date = paper["updated_date"]
        if pub_date==update_date:
            entry += f"- **⏳发布**：{pub_date}  \n"
        else:
            entry += f"- **⏳发布**：{pub_date}（更新：{update_date}）  \n"

        # 作者
        authors = paper["authors"]
        if len(authors) > 5:
            authors_str = ", ".join(authors[:3]) + " et al."
        else:
            authors_str = ", ".join(authors)
        entry += f"- **🧑‍🔬作者**：{authors_str}  \n"

        #被引
        #citations =paper["citations"]
        #entry += f"- **📚被引**：{citations}  \n"

        #comment
        comment=paper["comment"]
        entry += f"- **📝说明**：{comment}  \n"

        # 链接
        links = []
        # arXiv Abstract链接
        links.append(f"[arXiv Abstract](https://arxiv.org/abs/{arxiv_id})  ")

        # arXiv PDF链接
        # links.append(f"[arXiv PDF](https://arxiv.org/pdf/{arxiv_id}.pdf)  ")

        # GitHub链接
        if paper.get("github_url"):
            links.append(f"[GitHub]({paper['github_url']})")

        # 项目链接
        if paper.get("project_url"):
            links.append(f"[Project]({paper['project_url']})")
        elif paper["abstract"]:
            # 尝试从摘要中提取项目链接
            urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', paper["abstract"])
            for url in urls:
                if not url.startswith('http'):
                    url = 'https://' + url
                if 'arxiv.org' not in url and 'github.com' not in url:
                    links.append(f"[Project]({url})")
                    break

        entry += f"- **🔗链接**：{' · '.join(links)}  \n"

        # 摘要
        abstract = paper["abstract"]
        # 简略摘要（最多300词）
        words = abstract.split()
        if len(words) > 300:
            abstract = ' '.join(words[:300]) + " ..."
        entry += f"- **📝摘要**：{abstract}  \n"

        # 中文摘要（如果存在）
        if "abstract_zh" in paper and paper["abstract_zh"]:
            abstract_zh = paper["abstract_zh"]
            # 检查翻译失败的情况
            if "[翻译失败]" not in abstract_zh and "[翻译错误]" not in abstract_zh:
                # 限制中文摘要长度
                if len(abstract_zh) > 1000:
                    abstract_zh = abstract_zh[:1000] + "..."
                entry += f"- **📝翻译**: {abstract_zh}  \n\n"
            else:
                entry += f"- **📝翻译失败**: {abstract_zh}  \n\n"
        else:
            entry += "- **📝翻译未启用或未翻译**  \n\n"

        return entry

    except Exception:
        # 如果处理出错，返回空行
        return ""


def generate_markdown_content(papers_by_month: dict) -> str:
    """生成Markdown内容（包含翻译说明）"""
    # 标题
    markdown = "# 3D Gaussian Splatting 论文列表\n\n"
    markdown += "> **最后更新**： " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

    # 翻译说明
    markdown += "> **翻译说明**： 摘要有300字数限制（可修改），中文摘要由Edge浏览器翻译API自动生成，可能存在不准确之处。"
    markdown += "如需查看精确表达请参考原文摘要。\n\n"

    # 按月分组并按时间倒序排列
    sorted_months = sorted(
        papers_by_month.keys(),
        key=lambda m: datetime.datetime.strptime(m, "%B %Y"),
        reverse=True
    )

    # 添加论文数据
    for month in sorted_months:
        # 添加月份标题
        markdown += f"\n## {month}\n\n"

        # 按月内日期倒序排列论文
        papers = sorted(
            papers_by_month[month],
            key=lambda x: datetime.datetime.strptime(x["published_date"], "%Y-%m-%d"),
            reverse=True
        )

        # 添加每篇论文
        for index, paper in enumerate(papers, start=1):
            markdown += format_paper_entry(paper, index)

    return markdown


def get_last_update_time(update_dir: Path) -> str:
    """获取上一次的更新时间（精确到秒）"""
    # 查找最新的更新日志文件
    update_files = list(update_dir.glob("update_*.md"))
    if not update_files:
        return "无记录"

    # 按日期排序找到最新的文件
    latest_update_file = max(update_files, key=lambda f: f.stat().st_mtime)

    try:
        with open(latest_update_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("**本次更新时间**:"):
                    # 提取完整的时间字符串（精确到秒）
                    return line.split(":", 1)[1].strip()
    except Exception:
        pass
    return "未知时间"


def get_paper_id(paper: dict) -> str:
    """获取论文的唯一标识符（只取arXiv ID前10个字符）"""
    arxiv_url = paper["arxiv_url"]
    # 提取 arXiv ID 和版本号（如果有）
    match = re.search(r'arxiv\.org/abs/([\d\.v]+)', arxiv_url)
    if match:
        full_id = match.group(1)
        # 只取前10个字符作为唯一标识（去掉版本号）
        return full_id[:10]
    # 如果无法提取，使用标题作为备选
    return paper["title"][:10].replace(" ", "_")

def get_paper_state(paper: dict) -> tuple:
    """获取论文的关键状态信息用于比较"""
    return (
        clean_text(paper["title"]),  # 使用清洗后的标题
        paper["arxiv_url"].split('/')[-1],
        paper["updated_date"],
        clean_text(paper["comment"])
    )


def get_paper_changes(current_papers: list, last_papers: list) -> tuple:
    """找出新增和更新的论文"""
    # 第一次运行没有历史记录
    if not last_papers:
        return current_papers, []

    # 创建索引：paper_id -> paper_state
    last_papers_map = {}
    for paper in last_papers:
        paper_id = get_paper_id(paper)
        last_papers_map[paper_id] = get_paper_state(paper)

    # 创建当前论文索引
    current_papers_map = {}
    for paper in current_papers:
        paper_id = get_paper_id(paper)
        current_papers_map[paper_id] = get_paper_state(paper)

    # 找出新增论文（存在于当前但不存在于历史）
    new_papers = [
        paper for paper in current_papers
        if get_paper_id(paper) not in last_papers_map
    ]

    # 找出更新论文（存在于两者但状态不同）
    updated_papers = []
    for paper in current_papers:
        paper_id = get_paper_id(paper)
        if paper_id in last_papers_map:
            current_state = get_paper_state(paper)
            last_state = last_papers_map[paper_id]

            # 检查标题、arXiv ID或更新时间是否变化
            if current_state != last_state:
                # 记录变更详情
                changes = []
                if current_state[0] != last_state[0]:
                    changes.append("标题变更")
                if current_state[1] != last_state[1]:
                    changes.append("arXiv版本更新")
                if current_state[2] != last_state[2]:
                    changes.append("更新日期变化")
                if current_state[3] != last_state[3]:
                    changes.append("说明变更")

                updated_papers.append({
                    "paper": paper,
                    "changes": changes,
                    "previous_title": last_state[0],
                    "previous_version": last_state[1],
                    "previous_updated": last_state[2],
                    "previous_comment": last_state[3]
                })

    return new_papers, updated_papers

def clean_text(title: str) -> str:
    """清理多余空格和换行符"""
    # 去除首尾空白（包括换行符）后，替换中间换行符为空格
    return re.sub(r'\s+', ' ', title.strip().replace('\n', ' '))


def generate_update_log(last_update_time: str, new_papers: list, updated_papers: list) -> str:
    """生成更新日志内容"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"# 论文更新日志  \n\n"
    log += f"**上次更新时间**: {last_update_time}  \n"
    log += f"**本次更新时间**: {current_time}  \n"
    log += f"**新增论文数量**: {len(new_papers)}  \n"
    log += f"**变更论文数量**: {len(updated_papers)}  \n\n"

    if new_papers or updated_papers:
        log += "## 更新详情  \n"

        if new_papers:
            log += "\n### 新增论文  \n"
            for i, paper in enumerate(new_papers, start=1):
                # 清理标题中的多余空格和换行符
                title = clean_text(paper['title'])
                paper_id = paper["arxiv_url"].split('/')[-1]
                log += f"#### **{i}. [{title}]({paper['arxiv_url']})**"
                log += f" (ID: {paper_id})\n\n"

        if updated_papers:
            log += "\n### 变更论文  \n"
            for i, update_info in enumerate(updated_papers, start=1):
                paper = update_info["paper"]
                # 清理标题中的多余空格和换行符
                title = clean_text(paper['title'])
                paper_id = paper["arxiv_url"].split('/')[-1]

                log += f"#### **{i}. [{title}]({paper['arxiv_url']})** (ID: {paper_id})  \n"
                log += f"   **变更类型**: {', '.join(update_info['changes'])}  \n"

                # 清理原标题中的多余空格和换行符
                previous_title = clean_text(update_info['previous_title'])

                # 显示具体变更
                if "标题变更" in update_info["changes"]:
                    log += f" 🏷️原标题: {previous_title}  \n"
                    log += f" 🏷️新标题: {title}  \n"

                if "arXiv版本更新" in update_info["changes"]:
                    log += f" 📘原版本: v{update_info['previous_version'].split('v')[-1]}  \n"
                    log += f" 📘新版本: v{paper_id.split('v')[-1]}  \n"

                if "更新日期变化" in update_info["changes"]:
                    log += f" ⏳原更新: {update_info['previous_updated']}  \n"
                    log += f" ⏳新更新: {paper['updated_date']}  \n"

                if "说明变更" in update_info["changes"]:
                    log += f" 📝原说明: {update_info['previous_comment']}  \n"
                    log += f" 📝新说明: {paper['comment']}  \n"

                log += "\n"

    return log


def save_update_log(update_dir: Path, content: str):
    """保存更新日志到文件，文件名包含日期"""
    # 确保更新目录存在
    update_dir.mkdir(parents=True, exist_ok=True)

    # 生成文件名
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"update_{current_date}.md"
    file_path = update_dir / filename

    # 写入文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path


def save_cumulative_update_log(update_dir: Path, content: str):
    """将更新日志内容追加到累积更新日志文件（添加时间戳）"""
    cumulative_path = update_dir / "update_log.md"

    # 确保更新目录存在
    update_dir.mkdir(parents=True, exist_ok=True)

    # 从传入内容中提取最后两行（发现有误，不能直接取最后两行）
    # content_lines = content.splitlines()
    # last_two_lines = "\n".join(content_lines[-3:-1]) if len(content_lines) >= 3 else content

    # 为当前更新内容添加时间戳标题
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamped_content = f"# {timestamp}\n\n{content}"  #全文都加到日志里，也可以选择只记录两行

    # 添加分隔线
    separator = "\n\n---\n\n"

    # 如果文件不存在，创建新文件
    if not cumulative_path.exists():
        with open(cumulative_path, "w", encoding="utf-8") as f:
            f.write(timestamped_content)
        return

    # 读取现有内容
    with open(cumulative_path, "r", encoding="utf-8") as f:
        existing_content = f.read()

    # 将带时间戳的新内容添加到开头
    with open(cumulative_path, "w", encoding="utf-8") as f:
        f.write(timestamped_content)
        f.write(separator)
        f.write(existing_content)


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='生成论文列表和更新日志')
    parser.add_argument('--data-dir', type=str, default='../data',
                        help='论文数据目录路径')
    parser.add_argument('--output', type=str, default='../README.md',
                        help='README输出文件路径')
    parser.add_argument('--update-dir', type=str, default='../update',
                        help='更新日志目录路径')
    parser.add_argument('--translate', action='store_true',
                        help='启用摘要翻译功能（需要互联网连接）')
    args = parser.parse_args()

    # 创建路径对象
    data_dir = Path(args.data_dir)
    output_path = Path(args.output)
    update_dir = Path(args.update_dir)

    # 历史论文数据文件路径
    last_papers_file = data_dir / "last_papers.json"

    # 加载论文数据
    papers = load_latest_papers(data_dir)
    if not papers:
        print("没有找到论文数据，无法生成README")
        sys.exit(1)

    # ===== 更新日志逻辑 =====
    # 1. 获取上一次更新时间
    last_update_time = get_last_update_time(update_dir)

    # 2. 加载上一次的论文数据
    last_papers = []
    if last_papers_file.exists():
        try:
            with open(last_papers_file, "r", encoding="utf-8") as f:
                last_papers = json.load(f)
        except Exception as e:
            print(f"加载历史论文数据失败: {e}")

    # 3. 找出新增和更新的论文
    new_papers, updated_papers = get_paper_changes(papers, last_papers)

    # 4. 生成更新日志内容
    update_content = generate_update_log(last_update_time, new_papers, updated_papers)

    # 5. 保存更新日志文件
    update_path = save_update_log(update_dir, update_content)

    # 6. 将更新内容追加到累积更新日志文件
    save_cumulative_update_log(update_dir.parent, update_content)

    # 7. 保存当前论文数据作为下一次的历史数据
    try:
        with open(last_papers_file, "w", encoding="utf-8") as f:
            json.dump(papers, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存当前论文数据失败: {e}")
    # ===== 更新日志逻辑结束 =====

    # 直接启用翻译功能（内置开关）
    #enable_translation = False  # 如果要禁用，改为False

    # 如果启用翻译,命令行控制
    if args.translate:
        print("启用摘要翻译功能...")
        try:
            translator = EdgeTranslator()
            papers = translate_papers_abstracts(papers, translator)
        except Exception as e:
            print(f"翻译过程中发生错误，部分摘要可能未翻译: {str(e)}")
    else:
        print("跳过摘要翻译")

    # 按月份分组论文
    papers_by_month = group_papers_by_month(papers)
    print(f"按月份分组论文: {list(papers_by_month.keys())}")

    # 生成Markdown内容
    markdown_content = generate_markdown_content(papers_by_month)

    # 确保输出目录存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 写入README文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"成功生成README文件: {output_path}")
    print(f"成功生成更新日志: {update_path}")


if __name__ == "__main__":
    main()

