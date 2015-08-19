# http2sh
A terrible hack to send parameters to a shell command

Warning: This piece of software is horribly insecure.

http2sh is designed to take a URL that is provided to it, and execute a shell command with those parameters. It splits the URL into it's component path segments (separated by '/') and passes each segment as a separate argument.

In addition, it takes any command line arguments passed when it is started, and uses them as initial arguments.

### Examples

( Here we use lines starting withe '>' to denote URLs that are accessed, lines starting with '#' to denote start up parameters, and all other lines are command run. )

```
#
> http://localhost:4000/hello world/
echo 'hello world' ''
```
Three things about this example:

 * default port is 4000
 * default initial command is 'echo'
 * a trailing slash adds an empty parameter

```
# --port 7777 echo Hello
> http://localhost:7777/world/!
echo 'Hello' 'world' '!'
```

You can change the port it runs on, and the initial command arguments.

```
# cat
> http://localhost:4000/\etc\passwd
cat '\etc\passwd'
```

Oh, that's scary, isn't it?

It gets a little scarier...

```
# --split | cat
> http://localhost:4000/etc/passwd
cat 'etc/passwd'
```

The argument --split changes the string that is used to split the path into arguments. Also notice that the leading '/' is removed. This is because the split string defaults to "/", and would create an empty first argument. Rather than remove the first argument (and have to check if the split string is "/" or not) we just remove the leading "/" every time. This removal happens before string splitting.

```
# --no-strip --split | cat
> http://localhost:4000/etc/passwd
cat '/etc/passwd'
```

The `--no-strip` flag stops removing the leading '/' character from the path.
