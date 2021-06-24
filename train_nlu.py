from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')


train('data/nlu.md', 'config/config.yml', 'models/nlu')

interpreter = Interpreter.load('./models/nlu/default/chat')

# Ham test NLU
def ask_question(text):
    print(interpreter.parse(text))

# ask_question("nay có gì")
ask_question("cho anh tin bài viết số  1 này đi")
# ask_question("hôm nay có gì mới")
# ask_question("cho tôi lịch tháng này")
# ask_question("hôm nay có sự kiện gì mới")
# ask_question("Lịch trình hôm nay có gì?")