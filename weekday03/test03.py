class dispatcher():
    cmds = {}

    def reg(cmd, fn):
        if isinstance(cmd, str):
            cmds[cmd] = fn
        else:
            print('error')

    def run(self):
        while True:
            cmd = input('plz input command: ')
            if cmd.strip() == 'quit':
                return
            cmds.get(cmd.strip(), defaultfn())

    def defaultfn(self):
        pass


reg, run = dispatcher()

reg('cmd1', lambda: 1)
reg('cmd1', lambda: 2)

run()
