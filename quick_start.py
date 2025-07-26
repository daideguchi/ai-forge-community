#!/usr/bin/env python3
"""
AI Forge クイックスタートスクリプト
最小限の設定で即座に動作確認
"""

import os
import sys
import asyncio
from pathlib import Path

def create_minimal_env():
    """最小限の.envファイルを作成"""
    env_content = """# AI Forge 最小設定
# 以下の値を実際の値に置き換えてください

# Discord Bot Configuration (必須)
DISCORD_TOKEN=your_discord_bot_token_here
DISCORD_GUILD_ID=your_server_id_here

# AI API Keys (オプション - 機能を有効にする場合)
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# GitHub Configuration (Code Reviewer用)
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO_OWNER=your_username
GITHUB_REPO_NAME=your_repo_name

# Webhook URLs (GitHub連携用)
GITHUB_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_url/github

# RSS Feeds (Paper Summarizer用)
ARXIV_RSS_URLS=http://export.arxiv.org/rss/cs.AI,http://export.arxiv.org/rss/cs.LG

# Moderation Settings (Moderator用)
PERSPECTIVE_API_KEY=your_google_perspective_api_key
TOXICITY_THRESHOLD=0.7

# Database (本番環境用)
DATABASE_URL=sqlite:///ai_community.db
DB_PASSWORD=your_secure_password
"""
    
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ .env ファイルを作成しました")
    print("📝 .env ファイルを編集して、実際の値を設定してください")

def check_dependencies():
    """依存関係チェック"""
    print("📦 依存関係をチェック中...")
    
    required_packages = [
        'discord.py',
        'openai',
        'feedparser',
        'python-dotenv',
        'requests',
        'aiohttp'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'discord.py':
                import discord
            elif package == 'python-dotenv':
                import dotenv
            else:
                __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    if missing_packages:
        print(f"\n📥 以下のパッケージをインストールしてください:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def show_setup_guide():
    """セットアップガイドを表示"""
    print("\n🚀 AI Forge クイックスタートガイド")
    print("=" * 50)
    
    print("\n1️⃣  Discord Bot の作成:")
    print("   https://discord.com/developers/applications")
    print("   - New Application → Bot → Token をコピー")
    print("   - OAuth2 → URL Generator → bot, applications.commands")
    print("   - Bot Permissions: Send Messages, Use Slash Commands, Embed Links")
    
    print("\n2️⃣  Discord サーバーの準備:")
    print("   以下のチャンネルを作成:")
    print("   - #paper-summaries (論文要約)")
    print("   - #code-review-queue (コードレビュー)")
    print("   - #ai-training (AI学習)")
    print("   - #mod-log (モデレーション)")
    
    print("\n3️⃣  API キーの取得 (オプション):")
    print("   - OpenAI: https://platform.openai.com/")
    print("   - GitHub: Settings → Developer settings → Personal access tokens")
    print("   - Google Perspective: https://developers.perspectiveapi.com/")
    
    print("\n4️⃣  起動方法:")
    print("   # 単体Bot起動")
    print("   python start_paper_bot.py")
    print("   ")
    print("   # 全Bot起動")
    print("   python run_all_bots.py")
    print("   ")
    print("   # Docker起動")
    print("   docker-compose up -d")

def create_demo_data():
    """デモ用データを作成"""
    demo_dir = Path("demo")
    demo_dir.mkdir(exist_ok=True)
    
    # デモ用論文データ
    demo_paper = {
        "title": "Attention Is All You Need",
        "authors": "Ashish Vaswani, Noam Shazeer, Niki Parmar",
        "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
        "arxiv_id": "1706.03762",
        "published_date": "2017-06-12"
    }
    
    import json
    with open(demo_dir / "sample_paper.json", 'w', encoding='utf-8') as f:
        json.dump(demo_paper, f, ensure_ascii=False, indent=2)
    
    print("✅ デモデータを作成しました: demo/sample_paper.json")

async def test_basic_functionality():
    """基本機能のテスト"""
    print("\n🧪 基本機能テスト中...")
    
    try:
        # データベーステスト
        sys.path.append('bots/paper_summarizer')
        from bot import PaperDatabase
        
        db = PaperDatabase(":memory:")
        print("✅ データベース機能")
        
        # RSS解析テスト
        import feedparser
        feed = await asyncio.to_thread(feedparser.parse, "http://export.arxiv.org/rss/cs.AI")
        if feed.entries:
            print("✅ RSS フィード取得")
        else:
            print("⚠️  RSS フィード取得 (エントリなし)")
        
        print("✅ 基本機能テスト完了")
        
    except Exception as e:
        print(f"❌ 基本機能テストエラー: {e}")

def main():
    """メイン実行関数"""
    print("🎯 AI Forge クイックスタート")
    print("=" * 30)
    
    # .envファイルの確認・作成
    if not Path('.env').exists():
        print("📝 .env ファイルが見つかりません")
        create_minimal_env()
    else:
        print("✅ .env ファイルが存在します")
    
    # 依存関係チェック
    if not check_dependencies():
        print("\n❌ 依存関係が不足しています")
        print("実行してください: pip install -r requirements.txt")
        return
    
    # デモデータ作成
    create_demo_data()
    
    # 基本機能テスト
    try:
        asyncio.run(test_basic_functionality())
    except Exception as e:
        print(f"⚠️  テストスキップ: {e}")
    
    # セットアップガイド表示
    show_setup_guide()
    
    print("\n🎉 クイックスタート完了！")
    print("次のステップ:")
    print("1. .env ファイルを編集")
    print("2. Discord Bot を作成")
    print("3. python start_paper_bot.py で起動テスト")

if __name__ == "__main__":
    main()