import os

# main.pyのある、プロジェクト最上位のパス.
# ~/python_postgres_example
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# コンフィグのディレクトリのパス.
CONFIG_PATH = os.path.join(BASE_DIR, *["src", "config"])

# ログの設定ファイルのパス.
LOGINI_PATH = os.path.join(CONFIG_PATH, "log.ini")
