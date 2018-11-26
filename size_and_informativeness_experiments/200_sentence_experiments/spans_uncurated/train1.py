from model.data_utils1 import CoNLLDataset
from model.ner_model1 import NERModel
from model.base_model import BaseModel
from model.config1 import Config


def main():
    # create instance of config
    config = Config()

    # build model
    model = NERModel(config)
    model.build()
    # model.restore_session("results/crf/model.weights/") # optional, restore weights
    # model.reinitialize_weights("proj")

    # create datasets
    dev   = CoNLLDataset(config.filename_dev, config.processing_word,
                         config.processing_tag, config.max_iter)
    train = CoNLLDataset(config.filename_train, config.processing_word,
                         config.processing_tag, config.max_iter)

    # train model
    print('training')
    model.train(train, dev)

if __name__ == "__main__":
    main()
