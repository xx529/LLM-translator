import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.absolute()))

if __name__ == '__main__':

    from src.webpage import webpage

    webpage.run()
