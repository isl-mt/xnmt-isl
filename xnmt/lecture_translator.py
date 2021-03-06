# coding=utf-8

"""
This is the LT runtime binding, designed to make the ISL run-time variants of OpenNMT-py and XNMT swappable so that we
can load models trained with either toolkit in a seemless fashion via the lecture translator.
"""

import datetime
import socket
import sys

from xnmt import batchers, event_trigger
from xnmt.param_collections import ParamManager
from xnmt.persistence import initialize_if_needed, YamlPreloader, LoadSerialized

class OnlineTranslator(object):
  def __init__(self, model_file="/model/xnmt.mod"):
  # def __init__(self, model_file="examples/models/standard.mod"):

    exp_dir = "/tmp/"
    exp_name = f"xnmt-lt-{socket.gethostname()}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

    ParamManager.init_param_col()

    load_experiment = LoadSerialized( filename=model_file )

    uninitialized_experiment = YamlPreloader.preload_obj(load_experiment, exp_dir=exp_dir, exp_name=exp_name)
    self.loaded_experiment = initialize_if_needed(uninitialized_experiment)

    ParamManager.populate()
    event_trigger.set_train(val=False)
    self.idx = 0

  def translate(self, src_string: str) -> str:

    inp_sent = self.loaded_experiment.model.src_reader.read_sent(src_string, idx=self.idx)
    inp_sent_batch = batchers.mark_as_batch([inp_sent])
    event_trigger.start_sent(src=inp_sent_batch)
    translated_str = self.loaded_experiment.model.generate(src=inp_sent_batch,
                                                           search_strategy=self.loaded_experiment.model.inference.search_strategy)[0]
    self.idx += 1
    return translated_str.sent_str()

if __name__ == '__main__':
  sys.stdout.flush()
  t = OnlineTranslator()
  while True:
    line = sys.stdin.readline()
    #sys.stderr.write(f"got input: {line}\n")
    translation = t.translate(line)
    #sys.stderr.write(f"translated into: {translation}\n")
    print(translation)
    sys.stdout.flush()

#  for line in sys.stdin:
#    sys.stderr.write(f"got input: {line}\n")
#    translation = t.translate(line)
#    sys.stderr.write(f"translated into: {translation}\n")
#    sys.stdout.write(f"{translation}\n")OnlineTranslator().translate("hello world"))