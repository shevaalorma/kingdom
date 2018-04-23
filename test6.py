from pathlib import Path

p = Path('/etc')
print(str(p),bytes(p))

p = Path('/a/b/c/d')
print(p.parent.parent)
for x in p. parents:
    print(x)


p = Path('/magedu/mysqlinstall/mysql.tar.gz')
print(p.name)
print(p.suffix)
print(p.suffixes)
print(p.stem)
print(p.with_name('mysql-5.tgz'))
p = Path('README')
print(p.with_suffix('.txt'))