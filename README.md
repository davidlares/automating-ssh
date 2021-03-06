# Automating SSH connections

The following is a script for automating SSH connections via Python `Pexpect`.

According to the official docs, the `Pexpect` package works for controlling other applications and handling responses as if a human were typing commands. `Pexpect` Python scripts allow your script to `spawn child applications`, and its commonly used to perform connectivity tasks such as `SSH` or `FTP` connections and its human interactions.

I worked with a `Kali` and a `Metasploitable2` virtualized machine in order to use a compromised machine connected on a bridged-network (same subnet).

The command performed after the ssh connection is established, is the `cat /etc/shadow | grep root`. This file can be visible if you have `root` access privilege and the target machine will need to have the `22` port open (SSH port open).


## Set up

Simple, just.

`virtualenv -p python3 <name_of_the_env>`

## Usage

Preferable, use an isolated environment with `virtualenv`, because the `pexpect` package is required.

`ssh.py`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
