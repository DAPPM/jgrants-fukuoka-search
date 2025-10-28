import json
from datetime import datetime

def create_fukuoka_subsidies():
    """
    福岡県・福岡市の補助金データを作成
    ※実際の運用では、公式サイトからスクレイピングする
    """
    
    subsidies = [
        {
            "id": "fukuoka-pref-001",
            "title": "福岡県中小企業生産性向上支援補助金",
            "detail": "福岡県内の中小企業等が省力化又は省エネ化により生産性を向上させ、賃上げを行うために必要な設備投資等を支援する補助金です。",
            "subsidy_max_limit": 13000000,
            "subsidy_rate": "2/3以内",
            "acceptance_start_datetime": "2025-04-01T00:00:00Z",
            "acceptance_end_datetime": "2026-03-31T23:59:59Z",
            "target_area_search": "福岡県",
            "target_industry": "全業種",
            "inquiry_url": "https://www.pref.fukuoka.lg.jp/",
            "type": "県",
            "source": "福岡県",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "id": "fukuoka-city-001",
            "title": "福岡市ZEB・ZEH-M設計費補助金",
            "detail": "福岡市における建築物の脱炭素化を推進するため、省エネ性能の高い建物であるZEB（ゼブ）、ZEH-M（ゼッチマンション）の建設に係る設計費の定額補助を実施します。",
            "subsidy_max_limit": 3000000,
            "subsidy_rate": "定額",
            "acceptance_start_datetime": "2025-04-01T00:00:00Z",
            "acceptance_end_datetime": "2026-01-30T23:59:59Z",
            "target_area_search": "福岡市",
            "target_industry": "建設業",
            "inquiry_url": "https://www.city.fukuoka.lg.jp/",
            "type": "市",
            "source": "福岡市",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "id": "fukuoka-city-002",
            "title": "福岡市子育て世帯住替え助成事業",
            "detail": "子育てしやすい住宅への住替えを応援するために、賃貸住宅への引っ越しや中古住宅などの既存住宅の取得に関して最大25万円を助成します。",
            "subsidy_max_limit": 250000,
            "subsidy_rate": "定額",
            "acceptance_start_datetime": "2025-04-01T00:00:00Z",
            "acceptance_end_datetime": "2026-02-28T23:59:59Z",
            "target_area_search": "福岡市",
            "target_industry": "全業種",
            "inquiry_url": "https://www.city.fukuoka.lg.jp/",
            "type": "市",
            "source": "福岡市",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "id": "fukuoka-city-003",
            "title": "福岡市住宅用エネルギーシステム導入支援事業",
            "detail": "太陽光発電システム、蓄電池、V2Hシステム、高効率給湯器（エコキュート）、家庭用燃料電池などの導入費用を補助します。",
            "subsidy_max_limit": 200000,
            "subsidy_rate": "定額（システムにより異なる）",
            "acceptance_start_datetime": "2025-04-01T00:00:00Z",
            "acceptance_end_datetime": "2026-02-27T23:59:59Z",
            "target_area_search": "福岡市",
            "target_industry": "全業種",
            "inquiry_url": "https://www.city.fukuoka.lg.jp/",
            "type": "市",
            "source": "福岡市",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "id": "fukuoka-pref-002",
            "title": "福岡県地域中核企業成長促進事業",
            "detail": "地域中核企業が、新規事業展開等、成長に向けた新たな取組を実施していく上で必要な計画の策定など、その具体化を図る支援を行います。",
            "subsidy_max_limit": 1806000,
            "subsidy_rate": "2/3以内",
            "acceptance_start_datetime": "2025-08-04T00:00:00Z",
            "acceptance_end_datetime": "2025-12-26T23:59:59Z",
            "target_area_search": "福岡県",
            "target_industry": "全業種",
            "inquiry_url": "https://www.pref.fukuoka.lg.jp/",
            "type": "県",
            "source": "福岡県",
            "scraped_at": datetime.now().isoformat()
        }
    ]
    
    # JSONファイルに保存
    with open('fukuoka-subsidies.json', 'w', encoding='utf-8') as f:
        json.dump(subsidies, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {len(subsidies)}件の福岡県・市の補助金データを作成しました")
    print(f"📅 更新日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    create_fukuoka_subsidies()
