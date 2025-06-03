def cycle_crossover(parent1, parent2):
    """
    Implementează operatorul Cycle Crossover (CX) pentru permutări.
    
    Args:
        parent1, parent2: Liste reprezentând permutările părinților
    
    Returns:
        tuple: (child1, child2) - cei doi copii rezultați
    """
    n = len(parent1)
    child1 = [None] * n
    child2 = [None] * n
    
    # Găsește toate ciclurile
    visited = [False] * n
    cycle_number = 0
    
    for start in range(n):
        if not visited[start]:
            # Identifică ciclul curent
            cycle_positions = []
            pos = start
            
            while not visited[pos]:
                visited[pos] = True
                cycle_positions.append(pos)
                
                # Găsește unde este valoarea parent1[pos] în parent2
                value = parent1[pos]
                pos = parent2.index(value)
            
            # Aplică ciclul la copii
            for position in cycle_positions:
                if cycle_number % 2 == 0:  # Cicluri pare
                    child1[position] = parent1[position]
                    child2[position] = parent2[position]
                else:  # Cicluri impare
                    child1[position] = parent2[position]
                    child2[position] = parent1[position]
            
            cycle_number += 1
    
    return child1, child2


def print_cx_step_by_step(parent1, parent2):
    """Afișează pas cu pas aplicarea CX"""
    print("🔄 CYCLE CROSSOVER (CX) - Pas cu pas")
    print("=" * 50)
    print(f"Părinte X = {parent1}")
    print(f"Părinte Y = {parent2}")
    print()
    
    n = len(parent1)
    visited = [False] * n
    cycle_num = 1
    
    for start in range(n):
        if not visited[start]:
            print(f"🔍 Ciclul {cycle_num}:")
            cycle_positions = []
            pos = start
            cycle_path = []
            
            while not visited[pos]:
                visited[pos] = True
                cycle_positions.append(pos)
                value = parent1[pos]
                cycle_path.append(f"pos{pos}(X[{pos}]={value})")
                
                # Găsește următoarea poziție
                next_pos = parent2.index(value)
                if next_pos != start or len(cycle_positions) == 1:
                    pos = next_pos
                else:
                    break
            
            print(f"   Poziții: {cycle_positions}")
            print(f"   Traseu: {' → '.join(cycle_path)}")
            print()
            cycle_num += 1
    
    # Calculează copiii
    child1, child2 = cycle_crossover(parent1, parent2)
    
    print("🧬 Rezultatele:")
    print(f"C1 = {child1}")
    print(f"C2 = {child2}")
    
    # Verifică validitatea
    print("\n✅ Verificare:")
    print(f"C1 este permutare validă: {sorted(child1) == sorted(parent1)}")
    print(f"C2 este permutare validă: {sorted(child2) == sorted(parent1)}")


# Testează cu exemplul dat
if __name__ == "__main__":
    X = [6, 1, 8, 10, 5, 7, 9, 3, 4, 2]
    Y = [9, 8, 7, 3, 6, 1, 5, 10, 4, 2]
    
    print_cx_step_by_step(X, Y)
    
    print("\n" + "="*50)
    print("🧪 Test cu alt exemplu:")
    P1 = [1, 2, 3, 4, 5]
    P2 = [3, 4, 5, 2, 1]
    print_cx_step_by_step(P1, P2)
