def main():
    # Inicializar listas y variables
    bt = []  # bt (Burst Time) - Tiempo de ráfaga
    wt = []  # wt (Waiting Time) - Tiempo de espera
    tat = [] # tat (Turnaround Time) - Tiempo de retorno
    awt = 0.0  # Average Waiting Time
    atat = 0.0 # Average Turnaround Time

    n = int(input("Ingrese el número de procesos: "))

    # Solicitar el tiempo de ráfaga para cada proceso
    for i in range(n):
        tiempo = int(input(f"Ingrese el tiempo de ráfaga del proceso {i + 1}: "))
        bt.append(tiempo)
        wt.append(0)  # Inicializar wt con ceros
        tat.append(0) # Inicializar tat con ceros

    # --- Calcular el tiempo de espera (Waiting Time) ---
    # El primer proceso (índice 0) no espera
    wt[0] = 0

    # Calcular el tiempo de espera para los procesos restantes
    for i in range(1, n):
        # El tiempo de espera es la suma del tiempo de ráfaga del proceso anterior
        # más el tiempo de espera del proceso anterior.
        wt[i] = bt[i - 1] + wt[i - 1]

    # --- Calcular el tiempo de retorno (Turnaround Time) y los promedios ---
    for i in range(n):
        # Tiempo de retorno = Tiempo de ráfaga + Tiempo de espera
        tat[i] = bt[i] + wt[i]
        
        # Sumar a los totales para calcular el promedio después
        awt += wt[i]
        atat += tat[i]

    # --- Imprimir los resultados ---
    print("\nProceso\t\tbt\twt\tTAT")
    for i in range(n):
        print(f"P{i + 1}\t\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    # Calcular e imprimir los promedios
    print(f"\nTiempo promedio de espera = {awt / n:.2f}")
    print(f"Tiempo promedio de retorno = {atat / n:.2f}")

if __name__ == "__main__":
    main()