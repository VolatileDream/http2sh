# http2sh
A terrible hack to send paramaters to a shell command
---

Warning: This piece of software is horribly insecure.

http2sh is designed to take a URL that is provided to it, and execute a shell command with those parameters. It splits the URL into it's component path segments (seperated by '/') and passes each segment as a seperate argument.

In addition, it takes any command line arguments passed when it is started, and usses them as initial arguments.

### Examples

( Here we use lines starting withe '>' to denote URLs that are accessed, lines starting with '#' to denote startup parameters, and all other lines are command run. )

```
#
> http://localhost:4000/hello world
echo 'hello world' ''
```
Three things about this example:

 * default port is 4000
 * default initial command is 'echo'
 * no trailing slash is required

```
# --port 7777 echo Hello
> http://localhost:7777/world/!
echo 'Hello' 'world' '!'
```

You can change the port it runs on.

```
# cat
> http://localhost:4000/\etc\passwd
cat '\etc\passwd'
```

Oh, that's scary, isn't it?

It gets a little scarier...

```
# --remap ` cat
> http://localhost:4000/`etc`passwd
cat '/etc/passwd'
```

This software could easily be configured in a very bad way.
