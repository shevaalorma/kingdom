def command_dispatcher():
    global cmd_tb1, reg, defaultfunc, dispatcher
    cmd_tb1 = {}

    def reg(cmd):
        def _reg(fn):
            cmd_tb1[cmd] = fn
            return fn

        return _reg

    def defaultfunc():
        print("unkown  command")

    def dispatcher():
        while True:
            cmd = input(">>>")
            if cmd.strip() == '':
                return
            cmd_tb1.get(cmd, defaultfunc)()
    return reg,dispatcher

reg,dispatcher = command_dispatcher()
@reg('mage')
def foo1():
    print("mage")
@reg("py")
def foo2():
    print("python")

dispatcher()