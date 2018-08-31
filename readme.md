# Des'ree bot

## [@life_by_desree](https://twitter.com/life_by_desree).

This bot reads a line from Des'ree's prophetic smash hit [Life](https://www.youtube.com/watch?v=BKtrWU4zaaI) every ten minutes. You can see the twitter feed at [here](https://twitter.com/life_by_desree). It was inspired by the [africa by toto bot](https://twitter.com/africabytotobot), but this template can be used and adapted to tweet random lines from any file you want.

The setup is fairly simple: I have a Dreamhost account, a Python script, and a file I want to read from. The bot runs as a cron job from my Dreamhost account once every X minutes. 

Below are the bash instructions to set up this bot on Dreamhost. Most of the files have annotations.

You will need:

- A username on Dreamhost with access to SSH (or another web provider who'll let you use cron). Note that my username and password have been masked here as 'my-bot' and 'my-dreamhost-server' respectively
- A Twitter account set up with Developer credentials, and API keys (see [here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) for a nice tutorial)

Note that [this file](https://gist.github.com/moonmilk/8d78032debd16f31a8a9) was very useful in setting up my bot! 

Also note that Twitter now has rules about how many times you can post tweets with duplicate content. That means that a lot of the time, this code returns an error message saying that the message it wants to post is a duplicate tweet. If only Des' had written 80 verses like [Leonard Cohen](https://www.theguardian.com/music/2008/dec/19/leonard-cohen-hallelujah-christmas), this wouldn't have been such a problem! But then again, could anyone write that much about such a specific topic as _life_...?


## So, let's begin!

Log into your server via SSH
```ssh my-bot@my-dreamhost-server.dreamhost.com```
```# enter password```

Install Python3  
([detailed instructions here](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3)). Note that I'm doing this on a Mac, and it might be different on a PC or Linux. (I'm not sure, check the article. :) )

```bash
cd ~
mkdir tmp
cd tmp
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar zxvf Python-3.6.2.tgz 
cd Python-3.6.2 
./configure --prefix=$HOME/opt/python-3.6.2
make
make install
cd ~
nano .bash_profile
# add the following line
export PATH=$HOME/opt/python-3.6.2/bin:$PATH
# ctrl-O to save; enter to confirm; ctrl-x to close; now we're back to bash
# check we have the right python
which python3 
python3 --version
pip3 install --upgrade pip # just to be sure we're up to date
pip3 install virtualenv # not actually necessary, comes pre-installed with python 3
```

### Now to make the bot!
```
# cd into wherever you want to install first. in my case it's /Users/your-mac-username/Documents/github-root/bots/
virtualenv life-bot
cd life-bot
pip install tweepy
```

in a separate shell window
create a test file named ```test.py``` (just contains ```print("Hello World")```) on local machine
```
# cd to folder (note this is just where my bot is located)
cd /Users/your-mac-username/Documents/github-root/bots/life-bot/
# scp upload file
scp test.py my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/life-bot
# enter password
```

back to the ssh shell:

```
python test.py
```

if it prints "Hello World" - success!


### Now scrabble to write python code

I made several files:

- [life-bot.py](life-bot.py) - a script to post tweets
-  ```script.sh``` - a bash script to activate the virtualenv, run the python script with authentication, and then deactivate the virtualenv. this isn't included in GitHub as it has my bot credentials in it - you'll have to look through the [demo-script.sh.txt](demo-script.sh.txt) file here and make some changes to it with your credentials!
-  [life.txt](life.txt) - the file to read lines from (optional - the bot can also read from a list in the Python document)



- Change the demo-script.sh.txt to be named ```script.sh```
- Put your access keys, secrets and tokens into the bits marked ```YOUR_TOKEN_HERE``` etc
- Change the filepaths to point to the ones you set up earlier
- then ```scp``` entire folder to dreamhost (from non-ssh window):
```
scp * my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/life-bot
```

back to the ssh window! We need to make the script executable:
```
chmod +x script.sh
```
then test it:
```
./script.sh
```

If it works you'll see a tweet on your account. If not, something messed up and you need to google around and see what went wrong...

### Setting a Cron job on Dreamhost

See [here](https://help.dreamhost.com/hc/en-us/articles/215088668-How-do-I-create-a-cron-job-) for help with this 

This is my Cron command - it just fires up the cron in my [Dreamhost panel](https://panel.dreamhost.com/index.cgi?tree=advanced.cron&)
```
sh /home/my-bot/life-bot/script.sh > /dev/null
```
Mine runs every ten minutes. You can fire yours up whenever you like.

I hope this helps! Enjoy. :)
