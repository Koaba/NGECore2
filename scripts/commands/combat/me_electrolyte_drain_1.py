import sys

def setup(core, actor, target, command):
	core.buffService.addBuffToCreature(target, 'me_electrolyte_drain_1')
	return
	
def preRun(core, actor, target, command):
	return

def run(core, actor, target, commandString):
	return