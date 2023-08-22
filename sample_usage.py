from tqdm import tqdm
from avesta.similarity import similarity
import logging


def sample_similarity_checking():
    sim = similarity()
    logging.basicConfig()
    logger = logging.getLogger('Avesta')
    logger.setLevel(logging.INFO)
    logger.info("Start")
    data = open("shakespeare.txt", 'r').readlines()
    data = [line.strip() for line in data]
    all_similar_records = []
    for i in tqdm(data):
        for j in data:
            if i != j:
                if sim.char_based_similarity(i, j, threshold=17):
                    all_similar_records.append(i + '###' + j)

    logger.info("Number of similar records: " + str(len(all_similar_records)))


if __name__ == "__main__":
    sample_similarity_checking()
