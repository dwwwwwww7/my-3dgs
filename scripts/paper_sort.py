import json
import datetime
from pathlib import Path
import re
import argparse
from typing import List, Dict
from collections import defaultdict


class PaperSorter:
    def __init__(self):
        # 会议和期刊的映射字典（全称 -> 标准缩写）
        self.venue_mapping = {
            # ACM Multimedia 相关变体
            'ACM Multimedia': 'ACM MM',
            'ACMMM': 'ACM MM',
            'ACM MM': 'ACM MM',
            'ACM MULTIMEDIA': 'ACM MM',

            # TPAMI 相关变体
            'Transactions on Pattern Analysis and Machine Intelligence': 'TPAMI',
            'IEEE Transactions on Pattern Analysis and Machine Intelligence': 'TPAMI',
            'TPAMI': 'TPAMI',
            'PAMI': 'TPAMI',
            'IEEE TPAMI': 'TPAMI',

            # 其他常见会议和期刊
            'CVPR': 'CVPR',
            'Computer Vision and Pattern Recognition': 'CVPR',
            'ICCV': 'ICCV',
            'International Conference on Computer Vision': 'ICCV',
            'ECCV': 'ECCV',
            'European Conference on Computer Vision': 'ECCV',
            'SIGGRAPH': 'SIGGRAPH',
            'NeurIPS': 'NeurIPS',
            'Neural Information Processing Systems': 'NeurIPS',
            'NIPS': 'NeurIPS',
            'ICML': 'ICML',
            'International Conference on Machine Learning': 'ICML',
            'ICLR': 'ICLR',
            'International Conference on Learning Representations': 'ICLR',
            'AAAI': 'AAAI',
            'IJCAI': 'IJCAI',
            'WACV': 'WACV',
            'BMVC': 'BMVC',
            'ICASSP': 'ICASSP',
            'ICIP': 'ICIP',
            'ICRA': 'ICRA',
            'IROS': 'IROS',
            'TOG': 'TOG',
            'Transactions on Graphics': 'TOG',
            'TVCG': 'TVCG',
            'CVM': 'CVM',
            '3DV': '3DV',
            'ICME': 'ICME',
            'MICCAI': 'MICCAI',
            'MICLR': 'MICLR'
        }

        # 构建正则表达式模式
        self.conference_patterns = self._build_conference_patterns()

    def _build_conference_patterns(self):
        """构建支持多种变体的正则表达式模式"""
        patterns = []

        for full_name, std_name in self.venue_mapping.items():
            # 为每个会议/期刊创建灵活的模式
            if std_name == 'ACM MM':
                # ACM MM 的多种变体
                patterns.extend([
                    r'ACM\s*MM',  # ACM MM, ACM-MM, ACMMM
                    r'ACM\s*Multimedia',
                    r'ACMMM'  # 无空格的变体
                ])
            elif std_name == 'TPAMI':
                # TPAMI 的多种变体
                patterns.extend([
                    r'Transactions\s+on\s+Pattern\s+Analysis\s+and\s+Machine\s+Intelligence',
                    r'IEEE\s+Transactions\s+on\s+Pattern\s+Analysis\s+and\s+Machine\s+Intelligence',
                    r'TPAMI',
                    r'\bPAMI\b'
                ])
            else:
                # 其他会议的标准模式
                pattern = re.escape(full_name)
                patterns.append(pattern)

                # 也添加标准缩写
                if std_name != full_name:
                    patterns.append(re.escape(std_name))

        return patterns

    def _normalize_venue_name(self, matched_text: str) -> str:
        """将匹配到的文本标准化为统一的会议名称"""
        matched_lower = matched_text.lower().strip()

        # ACM MM 相关
        if any(pattern in matched_lower for pattern in ['acm mm', 'acmmm', 'acm multimedia']):
            return 'ACM MM'

        # TPAMI 相关
        elif any(pattern in matched_lower for pattern in ['transactions on pattern analysis', 'tpami', 'pami']):
            return 'TPAMI'

        # 其他会议的标准映射
        for full_name, std_name in self.venue_mapping.items():
            full_lower = full_name.lower()
            std_lower = std_name.lower()

            # 检查是否匹配全称或标准缩写
            if (full_lower in matched_lower or
                    std_lower in matched_lower or
                    matched_lower in full_lower or
                    matched_lower in std_lower):
                return std_name

        return matched_text.upper()

    def load_latest_papers(self, data_dir: Path) -> List[Dict]:
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

    def extract_conference_from_comment(self, comment: str) -> str:
        """从comment中提取会议名称，支持多种变体"""
        if not comment:
            return "Unknown"

        comment_clean = re.sub(r'[^\w\s]', ' ', comment)  # 移除标点符号，便于匹配

        # 尝试匹配会议名称
        best_match = None
        best_match_length = 0

        for pattern in self.conference_patterns:
            matches = re.finditer(pattern, comment_clean, re.IGNORECASE)
            for match in matches:
                matched_text = match.group()
                # 选择最长的匹配（通常更准确）
                if len(matched_text) > best_match_length:
                    best_match = matched_text
                    best_match_length = len(matched_text)

        if best_match:
            normalized_name = self._normalize_venue_name(best_match)
            return normalized_name

        # 如果没有找到匹配，尝试在标题中搜索
        return "Unknown"

    def extract_year_from_comment(self, comment: str) -> str:
        """从comment中提取年份，避免匹配URL中的数字"""
        if not comment:
            return "Unknown"

        # 首先移除URL部分，避免匹配URL中的数字
        url_pattern = r'https?://[^\s]+'
        comment_without_urls = re.sub(url_pattern, '', comment)

        # 查找4位数的年份，但排除明显是URL或代码的部分
        year_patterns = [
            r'\b(20\d{2})\b',  # 独立的年份
            r'(?<!\d)(20\d{2})(?!\d)',  # 确保前后不是数字
            r'(20\d{2})[^\d/]',  # 年份后不是数字或斜杠
        ]

        for pattern in year_patterns:
            year_match = re.search(pattern, comment_without_urls)
            if year_match:
                year = year_match.group(1) if year_match.groups() else year_match.group()
                if year.isdigit() and 2000 <= int(year) <= 2030:
                    return year

        return "Unknown"

    def sort_papers_by_year_and_conference(self, papers: List[Dict]) -> Dict:
        """按年份和会议分类论文"""
        sorted_papers = defaultdict(lambda: defaultdict(list))

        for paper in papers:
            # 从comment中提取会议和年份
            comment = paper.get("comment", "")
            conference = self.extract_conference_from_comment(comment)
            year_from_comment = self.extract_year_from_comment(comment)

            # 如果没有从comment中提取到年份，使用发布年份
            if year_from_comment == "Unknown":
                year = paper.get("published_date", "")[:4]  # 取前4位作为年份
                if not year or year == "":
                    year = "Unknown"
            else:
                year = year_from_comment

            # 为论文添加分类信息
            paper["conference_info"] = {
                "conference": conference,
                "year": year
            }

            # 按年份和会议分类
            sorted_papers[year][conference].append(paper)

        return sorted_papers

    def format_abstract(self, abstract: str, max_length: int = 1500) -> str:
        """格式化摘要，限制长度"""
        if not abstract:
            return ""

        if len(abstract) > max_length:
            return abstract[:max_length] + "..."
        return abstract

    def generate_conference_markdown(self, conference: str, year: str, papers: List[Dict]) -> str:
        """生成单个会议的Markdown文档"""
        # 标题
        markdown = f"# {conference} {year}\n\n"
        markdown += f"> **最后更新**： {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown += f"本页面包含 {year} 年 {conference} 会议的论文列表。\n\n"

        # 按月份排序论文
        papers_sorted = sorted(papers, key=lambda x: x.get("published_date", ""), reverse=True)

        for i, paper in enumerate(papers_sorted, 1):
            # 清理标题
            title = paper['title'].replace('\n', ' ').replace('  ', ' ').strip()
            arxiv_id = paper["arxiv_url"].split("/")[-1]

            # 作者
            authors = paper["authors"]
            if len(authors) > 5:
                authors_str = ", ".join(authors[:3]) + " et al."
            else:
                authors_str = ", ".join(authors)

            # 论文条目
            markdown += f"## {i}. {title}\n\n"
            markdown += f"- **作者**: {authors_str}\n"
            markdown += f"- **发布时间**: {paper['published_date']}\n"
            markdown += f"- **arXiv链接**: [arXiv:{arxiv_id}]({paper['arxiv_url']})\n"

            # GitHub链接（如果有）
            if paper.get("github_url"):
                markdown += f"- **代码链接**: [GitHub]({paper['github_url']})\n"

            # 说明（comment）
            comment = paper.get("comment", "")
            if comment:
                markdown += f"- **说明**: {comment}\n"

            # 英文摘要
            abstract_en = paper.get("abstract", "")
            if abstract_en:
                formatted_abstract = self.format_abstract(abstract_en)
                markdown += f"- **英文摘要**: {formatted_abstract}\n"

            # 中文摘要（如果有）
            abstract_zh = paper.get("abstract_zh", "")
            if abstract_zh and "[翻译失败]" not in abstract_zh and "[翻译错误]" not in abstract_zh:
                formatted_abstract_zh = self.format_abstract(abstract_zh)
                markdown += f"- **中文摘要**: {formatted_abstract_zh}\n"

            markdown += "\n---\n\n"

        return markdown

    def generate_year_index(self, year: str, conferences: Dict) -> str:
        """生成年份索引页面"""
        markdown = f"# {year} 年论文索引\n\n"
        markdown += f"> **最后更新**： {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown += f"本页面包含 {year} 年所有会议的论文索引。\n\n"

        # 会议统计
        total_papers = 0
        conference_stats = []

        for conference, papers in conferences.items():
            count = len(papers)
            total_papers += count
            conference_stats.append((conference, count))

        markdown += f"**总论文数**: {total_papers}\n\n"

        # 按论文数量排序
        conference_stats.sort(key=lambda x: -x[1])

        markdown += "## 会议列表\n\n"
        for conference, count in conference_stats:
            if count > 0 and conference != "Unknown":
                # 创建安全的文件名（替换空格和特殊字符）
                safe_conference_name = conference.replace(" ", "_").replace("/", "_")
                markdown += f"- [{conference} ({count}篇)]({safe_conference_name}.md)\n"

        # 未知会议
        if "Unknown" in conferences and conferences["Unknown"]:
            unknown_count = len(conferences["Unknown"])
            markdown += f"- [未归类会议 ({unknown_count}篇)](UnSorted.md)\n"

        return markdown

    def save_sorted_papers(self, sorted_papers: Dict, output_base_dir: Path):
        """保存按年份和会议分类的论文"""
        # 遍历每个年份
        for year, conferences in sorted_papers.items():
            if year == "Unknown":
                continue

            # 创建年份文件夹
            year_dir = output_base_dir / year
            year_dir.mkdir(parents=True, exist_ok=True)

            print(f"处理 {year} 年的论文...")

            # 生成年份索引页面
            year_index = self.generate_year_index(year, conferences)
            index_path = year_dir / "README.md"
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(year_index)

            # 为每个会议生成文档（只生成有论文的会议）
            for conference, papers in conferences.items():
                if not papers or conference == "Unknown":  # 跳过没有论文的会议和未知会议
                    continue

                # 生成会议文档
                conference_markdown = self.generate_conference_markdown(conference, year, papers)
                # 创建安全的文件名（替换空格和特殊字符）
                safe_conference_name = conference.replace(" ", "_").replace("/", "_")
                conference_filename = f"{safe_conference_name}.md"
                conference_path = year_dir / conference_filename

                with open(conference_path, "w", encoding="utf-8") as f:
                    f.write(conference_markdown)

                print(f"  - 生成 {conference}: {len(papers)} 篇论文")

            # 处理未知会议的论文
            if "Unknown" in conferences and conferences["Unknown"]:
                unknown_papers = conferences["Unknown"]
                unknown_markdown = self.generate_conference_markdown("未知会议", year, unknown_papers)
                unknown_path = year_dir / "Unknown.md"

                with open(unknown_path, "w", encoding="utf-8") as f:
                    f.write(unknown_markdown)

                print(f"  - 生成 未知会议: {len(unknown_papers)} 篇论文")

        # 处理Unknown年份的论文
        if "Unknown" in sorted_papers:
            unknown_year_dir = output_base_dir / "Unknown"
            unknown_year_dir.mkdir(parents=True, exist_ok=True)

            unknown_year_papers = []
            for conference, papers in sorted_papers["Unknown"].items():
                unknown_year_papers.extend(papers)

            if unknown_year_papers:
                # 按会议分类未知年份的论文
                unknown_year_conferences = defaultdict(list)
                for paper in unknown_year_papers:
                    conference = paper.get("conference_info", {}).get("conference", "Unknown")
                    unknown_year_conferences[conference].append(paper)

                # 生成未知年份的索引
                unknown_year_index = self.generate_year_index("未知年份", unknown_year_conferences)
                unknown_year_index_path = unknown_year_dir / "README.md"
                with open(unknown_year_index_path, "w", encoding="utf-8") as f:
                    f.write(unknown_year_index)

                # 为每个会议生成文档
                for conference, papers in unknown_year_conferences.items():
                    if not papers:
                        continue

                    conference_markdown = self.generate_conference_markdown(conference, "未知年份", papers)
                    safe_conference_name = conference.replace(" ", "_").replace("/", "_")
                    conference_filename = f"{safe_conference_name}.md"
                    conference_path = unknown_year_dir / conference_filename

                    with open(conference_path, "w", encoding="utf-8") as f:
                        f.write(conference_markdown)

                print(f"处理 未知年份 的论文: {len(unknown_year_papers)} 篇")

    def generate_main_index(self, sorted_papers: Dict, output_base_dir: Path):
        """生成主索引页面"""
        markdown = "# 3D Gaussian Splatting 论文分类索引\n\n"
        markdown += f"> **最后更新**： {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown += "本页面提供按年份和会议分类的论文索引。\n\n"

        # 统计信息
        total_papers = 0
        year_stats = []

        for year, conferences in sorted_papers.items():
            year_total = 0
            for conference, papers in conferences.items():
                year_total += len(papers)
            total_papers += year_total
            year_stats.append((year, year_total))

        markdown += f"**总论文数**: {total_papers}\n\n"

        # 按年份倒序排列
        year_stats.sort(key=lambda x: x[0] if x[0] != "Unknown" else "9999", reverse=True)

        markdown += "## 年份索引\n\n"
        for year, count in year_stats:
            if count > 0:
                if year == "Unknown":
                    markdown += f"- [未知年份 ({count}篇)](Unknown/README.md)\n"
                else:
                    markdown += f"- [{year}年 ({count}篇)]({year}/README.md)\n"

        # 保存主索引
        index_path = output_base_dir / "README.md"
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(markdown)


def main():
    parser = argparse.ArgumentParser(description='论文按年份和会议分类器')
    parser.add_argument('--data-dir', type=str, default='../data',
                        help='论文数据目录路径')
    parser.add_argument('--output-dir', type=str, default='../sorted_papers',
                        help='输出目录路径')
    args = parser.parse_args()

    # 创建路径对象
    data_dir = Path(args.data_dir)
    output_base_dir = Path(args.output_dir)
    output_base_dir.mkdir(parents=True, exist_ok=True)

    # 初始化分类器
    sorter = PaperSorter()

    # 加载论文数据
    papers = sorter.load_latest_papers(data_dir)
    if not papers:
        print("没有找到论文数据，无法统计")
        return

    # 按年份和会议分类论文
    print("开始按年份和会议分类论文...")
    sorted_papers = sorter.sort_papers_by_year_and_conference(papers)
    print("论文分类完成")

    # 保存分类的论文
    sorter.save_sorted_papers(sorted_papers, output_base_dir)

    # 生成主索引
    sorter.generate_main_index(sorted_papers, output_base_dir)

    print(f"\n所有处理完成！论文已按年份和会议分类到: {output_base_dir}")


if __name__ == "__main__":
    main()