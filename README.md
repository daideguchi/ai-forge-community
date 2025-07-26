# AI Forge - AI駆動開発コミュニティ

Discord と Git を連携させた AI 駆動開発コミュニティの構築プロジェクトです。

## 🚀 プロジェクト概要

このプロジェクトは段階的に以下の機能を実装していきます：

### Phase 1: 基盤構築 ✅
- [x] プロジェクト構造の作成
- [x] GitHub → Discord Webhook 通知
- [x] 基本的な Discord Bot セットアップ

### Phase 2: AI サービス ✅
- [x] 論文要約 RSS Bot
- [x] AI コードレビュー Bot
- [x] インテリジェントモデレーター
- [x] Human-in-the-Loop Bot (RLHF基盤)

### Phase 3: 高度な自動化
- [ ] IssueOps システム
- [ ] ペアプログラミング・マッチャー
- [ ] ハッカソン管理 Bot

### Phase 4: 未来のビジョン
- [ ] 分散型 AI ネットワーク
- [ ] RLHF コミュニティモデル
- [ ] AI エージェント実験場

## 📁 プロジェクト構造

```
ai-dev-community/
├── bots/                    # Discord Bot 実装
│   ├── paper-summarizer/    # 論文要約 Bot
│   ├── code-reviewer/       # コードレビュー Bot
│   └── moderator/          # モデレーション Bot
├── webhooks/               # Webhook 設定とスクリプト
├── github-actions/         # GitHub Actions ワークフロー
├── docs/                   # ドキュメント
└── config/                 # 設定ファイル
```

## 🛠️ 技術スタック

- **Discord Bot**: Python (discord.py)
- **AI/ML**: OpenAI API, Anthropic Claude
- **データベース**: SQLite (開発), PostgreSQL (本番)
- **CI/CD**: GitHub Actions
- **インフラ**: Docker, Railway/Heroku

## 🚀 クイックスタート

```bash
# 1. リポジトリをクローン
git clone https://github.com/daideguchi/ai-forge-community.git
cd ai-forge-community

# 2. 依存関係をインストール
pip install -r requirements.txt

# 3. 設定ガイド確認
python quick_start.py

# 4. Discord & API設定（重要！）
# 📖 DISCORD_SETUP.md - Discord完全設定
# 🔑 API_KEYS_SETUP.md - APIキー取得

# 5. 設定テスト
python test_api_keys.py

# 6. Bot起動
python start_paper_bot.py
```

## 📚 完全セットアップガイド

| ガイド | 内容 | 必須度 |
|--------|------|--------|
| [✅ COMPLETE_SETUP_CHECKLIST.md](COMPLETE_SETUP_CHECKLIST.md) | **完全チェックリスト** | **必須** |
| [📖 DISCORD_SETUP.md](DISCORD_SETUP.md) | Discord Bot作成・サーバー設定 | **必須** |
| [🔑 API_KEYS_SETUP.md](API_KEYS_SETUP.md) | 全APIキー取得方法 | **必須** |
| [🚀 DEPLOYMENT.md](DEPLOYMENT.md) | 本番環境デプロイ | オプション |
| [📋 docs/step1-paper-bot.md](docs/step1-paper-bot.md) | 詳細技術解説 | 参考 |

## 🌐 リポジトリ

**GitHub**: https://github.com/daideguchi/ai-forge-community

## ⚠️ 重要な注意

**設定を飛ばすとBotは絶対に動きません！**
- Discord設定（チャンネル作成、Bot招待）
- APIキー設定（OpenAI、GitHub等）
- 環境変数設定（.envファイル）

一つずつ確実に実行してください。

## 📋 詳細セットアップ

- **Step 1**: [Paper Summarizer Bot](docs/step1-paper-bot.md)
- **Step 2**: [Code Reviewer Bot](docs/setup-guide.md)
- **Step 3**: [Human-in-the-Loop Bot](docs/setup-guide.md)
- **Step 4**: [Moderator Bot](docs/setup-guide.md)

## 🤝 コントリビューション

このプロジェクトはコミュニティ駆動で開発されています。貢献方法については [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。