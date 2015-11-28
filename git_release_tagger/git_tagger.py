import envoy
import sys

class FailureStatusCodeException(Exception):
  def __init__(self, result):
    self.status_code = result.status_code
    self.std_out     = result.std_out
    self.std_err     = result.std_err

  def __str__(self):
    return """
Status Code: {status_code}
Standard Output: {std_out}
Standard Error: {std_err}
    """.format(status_code=self.status_code, std_out=self.std_out, std_err=self.std_err)

def _run_command(command, verbose=False, ignore_status_codes=False):
  if verbose:
    print command

  r = envoy.run(command, timeout=3600)

  if r.status_code != 0 and not ignore_status_codes:
    raise FailureStatusCodeException(r)

  return r

def list_tags():
  _run_command("git fetch origin 'refs/tags/*:refs/tags/*'")

  r = _run_command("git tag")
  return r.std_out.split()

def add_tag(tag, message="", cmd_options={}):
  command = "git tag -a '{tag}'".format(tag=tag)
  command += " -m '{message}'".format(message=message)

  _run_command(command, **cmd_options)

def remove_tags(tags, cmd_options={}):
  if not len(tags):
    return

  commands = [
    "git push --delete origin {}".format(
      " ".join(["'{}'".format(tag) for tag in tags])
    )
  ]

  for tag in tags:
    commands.append("git tag -d '{tag}'".format(tag=tag))

  for command in commands:
    _run_command(command, **cmd_options)

def push_tags(cmd_options={}):
  command = "git push --tags"
  _run_command(command, **cmd_options)
