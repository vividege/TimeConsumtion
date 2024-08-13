import os


class ContextManager:
    def __init__(self, old_path):
        self.old_path = old_path

    def __enter__(self):
        print("Enter context manager __enter__")
        return self.old_path

    def __exit__(self, *argc):
        os.chdir(self.old_path)


def change_dir(path):
    old_path = os.getcwd()
    os.chdir(path)
    return ContextManager(old_path)


if __name__ == '__main__':
    tmp = change_dir("C:\\Users\\hlxiao\\Documents\\Downloads")
    with tmp as old_dir:  # with 后面要求跟ContextMananger对象，所以tmp是一个contextManager对象，该对象的__enter__()函数的返回值传给as后面的变量
        # __enter__()函数执行完成，进入with的主体
        print(f"old dir: {old_dir}")
        print(f"current dir: {os.getcwd()}")
    # with 语句退出时执行contextManager的__exit__（）方法
    print(f"After with dir is: {os.getcwd()}")
