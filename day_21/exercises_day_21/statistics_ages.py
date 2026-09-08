from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        counts = Counter(self.data)
        mode_val, count_val = counts.most_common(1)[0]
        return {'mode': mode_val, 'count': count_val}

    def var(self):
        mean_val = self.sum() / self.count()
        # Sample variance formula (n - 1)
        variance = sum((x - mean_val) ** 2 for x in self.data) / (self.count() - 1)
        return round(variance, 1)

    def std(self):
        # Calculating standard deviation directly from unrounded variance
        mean_val = self.sum() / self.count()
        variance = sum((x - mean_val) ** 2 for x in self.data) / (self.count() - 1)
        return round(math.sqrt(variance), 1)

    def freq_dist(self):
        counts = Counter(self.data)
        total = self.count()
        # Calculate percentage for each item and sort by frequency descending
        freqs = [(round((count / total) * 100, 1), val) for val, count in counts.items()]
        freqs.sort(key=lambda x: x[0], reverse=True)
        return freqs

    def describe(self):
        mode_info = self.mode()
        freq_str = str(self.freq_dist())
        
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: ({mode_info['mode']}, {mode_info['count']})\n"
            f"Variance: {self.var()}\n"
            f"Standard Deviation: {self.std()}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


# Example Usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

print("\n" + "="*40 + "\n")
print(data.describe())