class SysCall:
    def __init__(self, kernel):
        self.kernel = kernel

    def log(self, text):
        print(f"[SYS] {text}")

    def open_app(self, appname):
        self.log(f"Launching {appname}")
        return self.kernel.create_process(appname)
