import os, sys

# 客户端启动入口
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.script import run

if __name__ == '__main__':
    run()
