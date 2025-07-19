# This is my second test file to upload to Github
import pandas as pd

data = {"line1": [1,2,3,4,5,6],
        "line2": [6,7,8,9,10,11]}

df = pd.DataFrame(data)

print(df) 




# bar chart
movies = ["Movie A", "Movie B", "Movie C"]
ratings = [8.5, 7.2, 9.0]
import matplotlib.pyplot as plt
plt.bar(range(len(movies)), ratings)

plt.title("My Movie Ratings")
plt.xlabel("Movies")
plt.ylabel("Ratings")

plt.show()