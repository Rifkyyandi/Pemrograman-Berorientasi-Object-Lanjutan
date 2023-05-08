from joblib import Parallel, delayed
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
if __name__ == '__main__':
    # Panggil fungsi worker secara parallel
    Parallel(n_jobs=2)(delayed(worker)(i) for i in range(5))