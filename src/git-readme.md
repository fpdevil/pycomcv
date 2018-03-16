# Git: pushing to and pulling from multiple remote locations: remote, url and pushurl

*When pushing to or pulling from a remote url in git, the meaning of –all seems to be different between when git push –all is invoked and when calling git pull –all. Here’s an empirically obtained understanding of how you can configure git to push to and/or pull from multiple remote urls.*

*When git push –all is called, git will push all branches to the default remote. When invoking git pull –all, git will pull from the first url listed in all remotes.*

- Pushing to multiple remote urls

>*If you want to push to multiple remote urls, you need only one remote containing multiple urls, and your .git/config should contain something like* :+1:

```
[remote "Location1"]
  url   = git@url1.org/code.git
  url   = git@url2.org/code.git
  fetch = +refs/heads/*:refs/remotes/Location1/*
[ branch "master"]
  remote  = Location1
  merge   = refs/heads/master
```

- *From the command line, this can be achieved by:*


```shell
$ git remote add Location1 git@url1.org/code.git
$ git remote set-url --add Location1 git@url2.org/code.git
$ git push -vu Location1 master

# and checked by:

$ git remote -v
Location1  git@url1.org/code.git (fetch)
Location1  git@url1.org/code.git (push)
Location1  git@url2.org/code.git (push)

# Hence, when issuing git push, it will push to url1 and url2, when doing git pull, the repository will be pulled (fetched) only from url1.
```


- *Pulling from multiple remote urls*
> 
> Since git pull will pull only from the first url in the default remote, and git pull –all will pull form the first url of all remotes, you will need to configure one remote per url:

```shell
[remote "Location1"]
  url   = git@url1.org/code.git
  fetch = +refs/heads/*:refs/remotes/Location1/*
[remote "Location2"]
  url   = git@url2.org/code.git
  fetch = +refs/heads/*:refs/remotes/Location2/*
[ branch "master"]
  remote  = Location1
  merge   = refs/heads/master
```

- This is configured by:

```shell
$ git remote add Location1 git@url1.org/code.git
$ git remote add Location2 git@url2.org/code.git
$ git push -vu Location1 master
```

- Checking now gives

```shell
$ git remote -v
Location1  git@url1.org/code.git (fetch)
Location1  git@url1.org/code.git (push)
Location2  git@url2.org/code.git (fetch)
Location2  git@url2.org/code.git (push)
```

> *which is misleading, since git push will not push to url2.
Git will pull from url1 and url2 when issuing git pull –all, but only push to url1, since this is the only remote configured for the master branch (and only the last remote will be used if more than one is listed).*

- Pushing to and pulling from multiple remote urls

> *To both push to and pull from multiple remote locations (either the same or different ones for push and pull) we need one remote per location, and the default remote must contain one url per location. The example for two identical urls is:*

```shell
[remote "Location1"]
  url   = git@url1.org/code.git
  url   = git@url2.org/code.git
  fetch = +refs/heads/*:refs/remotes/Location1/*
[remote "Location2"]
  url   = git@url2.org/code.git
  fetch = +refs/heads/*:refs/remotes/Location2/*
[ branch "master"]
  remote  = Location1
  merge   = refs/heads/master

# This is configured by:

$ git remote add Location1 git@url1.org/code.git
$ git remote set-url --add Location1 git@url2.org/code.git
$ git remote add Location2 git@url2.org/code.git
$ git push -vu Location1 master

# Checking now gives:

$ git remote -v
Location1  git@url1.org/code.git (fetch)
Location1  git@url1.org/code.git (push)
Location1  git@url2.org/code.git (push)
Location2  git@url2.org/code.git (fetch)
Location2  git@url2.org/code.git (push)
```

>*and git push will push to both urls in Location1, while git pull –all will pull from url1 and url2, because they are the first ones listed in Location1 and Location2.*
