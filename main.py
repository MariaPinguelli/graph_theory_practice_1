from modules.graph_reader import read_and_format_data
from modules.eccentricity import calculate_eccentricity
from modules.closeness_centrality import calculate_closeness_centrality

def main():
    # Tratar dados de entrada
    read_and_format_data()
    # Calcular excentricidade do grafo
    calculate_eccentricity()
    # Calcular closeness centrality dos vértices
    calculate_closeness_centrality()

if __name__ == '__main__':
    main()