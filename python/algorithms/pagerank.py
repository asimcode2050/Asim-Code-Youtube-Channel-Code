import numpy as np
links = np.array([[0, 0, 1, 0],
                  [1, 0, 0, 0],
                  [1, 1, 0, 1],
                  [0, 0, 0, 0]])
n_pages = links.shape[0]
pagerank = np.ones(n_pages) / n_pages
damping_factor = 0.85
iterations = 100
for i in range(iterations):
    new_pagerank = np.zeros(n_pages)
    for page in range(n_pages):
        incoming_links = links[:, page]
        for other_page in range(n_pages):
            if incoming_links[other_page] > 0:
                new_pagerank[page] += pagerank[other_page] / \
                    np.sum(links[other_page])
    new_pagerank = damping_factor * new_pagerank + \
        (1 - damping_factor) / n_pages
    pagerank = new_pagerank
print("PageRank scores after {} iterations:".format(iterations))
for i, rank in enumerate(pagerank):
    print(f"Page {chr(65 + i)}: {rank:.4f}")
