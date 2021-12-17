from tempfile import NamedTemporaryFile, TemporaryDirectory
with TemporaryDirectory(dir='.') as tempdir:
    print('Temp Directory : ', tempdir)
    with NamedTemporaryFile(dir=tempdir) as tf:
        name = tf.name
        print(name)

