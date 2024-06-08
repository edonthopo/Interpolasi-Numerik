# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi Riemann
def riemann_integration(a, b, N):
    delta_x = (b - a) / N
    sum_integral = 0
    for i in range(N):
        x_i = a + i * delta_x
        sum_integral += f(x_i) * delta_x
    return sum_integral

# Fungsi untuk menghitung galat RMS secara manual
def rms_error(estimated_pi, true_pi):
    return ((estimated_pi - true_pi)**2) ** 0.5

# Fungsi untuk mengukur waktu eksekusi secara manual
def measure_time(func, *args):
    import time
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Nilai referensi pi
true_pi = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Pengujian
for N in N_values:
    estimated_pi, execution_time = measure_time(riemann_integration, 0, 1, N)
    error = rms_error(estimated_pi, true_pi)
    
    print(f"N = {N}")
    print(f"Estimated pi = {estimated_pi:.16f}")
    print(f"RMS error = {error:.16f}")
    print(f"Execution time = {execution_time:.6f} seconds")
    print("-" * 40)
