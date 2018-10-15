import datetime
import socket
import sys

from xnmt import batchers, event_trigger, logger, tee
from xnmt.param_collections import ParamManager
from xnmt.persistence import initialize_if_needed, YamlPreloader, LoadSerialized

class OnlineTranslator(object):
  # examples/models/standard.mod
  def __init__(self, model_file="/model/xnmt.mod", log_file="/tmp/xnmt.log"):

    # exp_dir = os.path.dirname(__file__)
    exp_dir = "/tmp/"
    exp_name = f"xnmt-lt-{socket.gethostname()}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    #log_file = f"{exp_dir}/logs/{exp_name}.log"

    tee.set_out_file(log_file, exp_name)
    logger.info(
      f"running XNMT revision {tee.get_git_revision()} "
      f"on {socket.gethostname()} "
      f"on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

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
    return translated_str

if __name__ == '__main__':
  sys.exit(OnlineTranslator().translate("hello world"))
