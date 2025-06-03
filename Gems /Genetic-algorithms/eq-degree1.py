import numpy as np
import matplotlib.pyplot as plt
import random
from typing import List, Tuple, Dict
import time

class GeneticLinearSolver:
    """
    Clasa pentru rezolvarea ecuațiilor de gradul 1 folosind algoritmi genetici.
    Ecuația: ax + b = c, găsim x
    """
    
    def __init__(self, a: float, b: float, c: float, 
                 pop_size: int = 50, 
                 mutation_rate: float = 0.1,
                 crossover_rate: float = 0.8,
                 search_range: float = 20.0):
        """
        Inițializează solverul genetic.
        
        Args:
            a, b, c: Coeficienții ecuației ax + b = c
            pop_size: Mărimea populației
            mutation_rate: Rata mutației (0-1)
            crossover_rate: Rata crossover-ului (0-1)
            search_range: Intervalul de căutare [-range, +range]
        """
        self.a = a
        self.b = b
        self.c = c
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.search_range = search_range
        
        # Soluția exactă pentru comparație
        self.exact_solution = (c - b) / a if a != 0 else float('inf')
        
        # Istoricul evoluției
        self.history = {
            'generations': [],
            'best_fitness': [],
            'best_solution': [],
            'average_fitness': [],
            'errors': []
        }
        
    def initialize_population(self) -> List[float]:
        """Generează populația inițială."""
        return [random.uniform(-self.search_range, self.search_range) 
                for _ in range(self.pop_size)]
    
    def fitness_function(self, x: float) -> float:
        """
        Calculează fitness-ul pentru o valoare x.
        Fitness mai mare = soluție mai bună.
        """
        # Calculăm cât de departe suntem de soluția corectă
        left_side = self.a * x + self.b
        error = abs(left_side - self.c)
        
        # Transformăm eroarea în fitness (mai mare = mai bun)
        return 1.0 / (1.0 + error)
    
    def evaluate_population(self, population: List[float]) -> List[Tuple[float, float]]:
        """
        Evaluează întreaga populație.
        Returns: Lista de tuple (individ, fitness)
        """
        return [(individual, self.fitness_function(individual)) 
                for individual in population]
    
    def tournament_selection(self, evaluated_pop: List[Tuple[float, float]], 
                           tournament_size: int = 3) -> float:
        """Selecția prin turnir."""
        tournament = random.sample(evaluated_pop, tournament_size)
        return max(tournament, key=lambda x: x[1])[0]  # Returnează individul cu cel mai mare fitness
    
    def arithmetic_crossover(self, parent1: float, parent2: float) -> Tuple[float, float]:
        """Crossover aritmetic între doi părinți."""
        if random.random() > self.crossover_rate:
            return parent1, parent2
        
        alpha = random.random()
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = alpha * parent2 + (1 - alpha) * parent1
        
        return child1, child2
    
    def gaussian_mutation(self, individual: float, mutation_strength: float = 0.5) -> float:
        """Mutația gaussiană."""
        if random.random() < self.mutation_rate:
            noise = np.random.normal(0, mutation_strength)
            return individual + noise
        return individual
    
    def evolve_generation(self, population: List[float]) -> List[float]:
        """Evoluează o generație completă."""
        # Evaluăm populația
        evaluated_pop = self.evaluate_population(population)
        evaluated_pop.sort(key=lambda x: x[1], reverse=True)  # Sortăm după fitness
        
        # Păstrăm elita (cei mai buni 10%)
        elite_size = max(1, int(self.pop_size * 0.1))
        new_population = [ind for ind, fit in evaluated_pop[:elite_size]]
        
        # Generăm restul populației prin crossover și mutație
        while len(new_population) < self.pop_size:
            parent1 = self.tournament_selection(evaluated_pop)
            parent2 = self.tournament_selection(evaluated_pop)
            
            child1, child2 = self.arithmetic_crossover(parent1, parent2)
            
            child1 = self.gaussian_mutation(child1)
            child2 = self.gaussian_mutation(child2)
            
            new_population.append(child1)
            if len(new_population) < self.pop_size:
                new_population.append(child2)
        
        return new_population
    
    def solve(self, max_generations: int = 1000, target_error: float = 1e-6, 
              verbose: bool = True) -> Dict:
        """
        Rulează algoritmul genetic pentru a rezolva ecuația.
        
        Args:
            max_generations: Numărul maxim de generații
            target_error: Eroarea minimă acceptabilă
            verbose: Afișează progresul
            
        Returns:
            Dicționar cu rezultatele
        """
        # Resetăm istoricul
        self.history = {key: [] for key in self.history.keys()}
        
        # Inițializăm populația
        population = self.initialize_population()
        
        start_time = time.time()
        
        for generation in range(max_generations):
            # Evaluăm populația curentă
            evaluated_pop = self.evaluate_population(population)
            evaluated_pop.sort(key=lambda x: x[1], reverse=True)
            
            # Cel mai bun individ din generația curentă
            best_individual, best_fitness = evaluated_pop[0]
            average_fitness = np.mean([fit for _, fit in evaluated_pop])
            
            # Calculăm eroarea
            current_error = abs(self.a * best_individual + self.b - self.c)
            
            # Salvăm în istoric
            self.history['generations'].append(generation)
            self.history['best_fitness'].append(best_fitness)
            self.history['best_solution'].append(best_individual)
            self.history['average_fitness'].append(average_fitness)
            self.history['errors'].append(current_error)
            
            # Afișăm progresul
            if verbose and (generation % 50 == 0 or generation < 10):
                print(f"Generația {generation:4d}: "
                      f"x = {best_individual:8.6f}, "
                      f"fitness = {best_fitness:.6f}, "
                      f"eroare = {current_error:.6f}")
            
            # Verificăm criteriul de oprire
            if current_error < target_error:
                if verbose:
                    print(f"\n🎯 CONVERGED! Eroarea {current_error:.8f} < {target_error}")
                break
            
            # Evoluăm către generația următoare
            population = self.evolve_generation(population)
        
        end_time = time.time()
        
        # Rezultatele finale
        final_result = {
            'best_solution': best_individual,
            'exact_solution': self.exact_solution,
            'error': current_error,
            'fitness': best_fitness,
            'generations': generation + 1,
            'execution_time': end_time - start_time,
            'converged': current_error < target_error
        }
        
        if verbose:
            self.print_results(final_result)
        
        return final_result
    
    def print_results(self, results: Dict):
        """Afișează rezultatele într-un format frumos."""
        print("\n" + "="*60)
        print(f"REZULTATELE ALGORITMULUI GENETIC")
        print("="*60)
        print(f"Ecuația: {self.a}x + {self.b} = {self.c}")
        print(f"Soluția exactă:      {results['exact_solution']:12.8f}")
        print(f"Soluția găsită:      {results['best_solution']:12.8f}")
        print(f"Eroarea absolută:    {results['error']:12.8f}")
        print(f"Fitness final:       {results['fitness']:12.8f}")
        print(f"Generații rulate:    {results['generations']:12d}")
        print(f"Timp de execuție:    {results['execution_time']:12.4f} secunde")
        print(f"Status:              {'CONVERGED' if results['converged'] else 'MAX GENERATIONS'}")
        print("="*60)
    
    def plot_evolution(self, save_plot: bool = False):
        """Desenează graficele evoluției algoritmului."""
        if not self.history['generations']:
            print("Nu există date pentru grafic. Rulați mai întâi solve().")
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        generations = self.history['generations']
        
        # Graficul 1: Evoluția fitness-ului
        ax1.plot(generations, self.history['best_fitness'], 'b-', label='Cel mai bun fitness', linewidth=2)
        ax1.plot(generations, self.history['average_fitness'], 'r--', label='Fitness mediu', alpha=0.7)
        ax1.set_xlabel('Generații')
        ax1.set_ylabel('Fitness')
        ax1.set_title('Evoluția Fitness-ului')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Graficul 2: Evoluția soluției
        ax2.plot(generations, self.history['best_solution'], 'g-', linewidth=2, label='Cea mai bună soluție')
        ax2.axhline(y=self.exact_solution, color='r', linestyle='--', 
                   label=f'Soluția exactă ({self.exact_solution:.6f})')
        ax2.set_xlabel('Generații')
        ax2.set_ylabel('Valoarea x')
        ax2.set_title('Convergența către Soluția Corectă')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Graficul 3: Evoluția erorii (scală logaritmică)
        ax3.semilogy(generations, self.history['errors'], 'purple', linewidth=2)
        ax3.set_xlabel('Generații')
        ax3.set_ylabel('Eroarea (scală log)')
        ax3.set_title('Reducerea Erorii în Timp')
        ax3.grid(True, alpha=0.3)
        
        # Graficul 4: Distribuția ultimei populații
        final_population = self.initialize_population()  # Pentru demonstrație
        final_evaluated = self.evaluate_population(final_population)
        solutions = [ind for ind, _ in final_evaluated]
        
        ax4.hist(solutions, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        ax4.axvline(x=self.exact_solution, color='red', linestyle='--', linewidth=2,
                   label=f'Soluția exactă')
        ax4.axvline(x=self.history['best_solution'][-1], color='green', linestyle='-', linewidth=2,
                   label='Cea mai bună soluție')
        ax4.set_xlabel('Valoarea x')
        ax4.set_ylabel('Frecvența')
        ax4.set_title('Distribuția Soluțiilor în Ultima Populație')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_plot:
            plt.savefig('genetic_algorithm_evolution.png', dpi=300, bbox_inches='tight')
            print("Graficul a fost salvat ca 'genetic_algorithm_evolution.png'")
        
        plt.show()

def run_examples():
    """Rulează câteva exemple de demonstrație."""
    print("🧬 DEMONSTRAȚIE: Algoritmi Genetici pentru Ecuații Liniare")
    print("="*70)
    
    examples = [
        (3, 7, 22),      # 3x + 7 = 22  =>  x = 5
        (2, -5, 11),     # 2x - 5 = 11  =>  x = 8
        (-4, 12, 0),     # -4x + 12 = 0 =>  x = 3
        (0.5, 2.3, 7.8)  # 0.5x + 2.3 = 7.8 => x = 11
    ]
    
    for i, (a, b, c) in enumerate(examples, 1):
        print(f"\n📝 EXEMPLUL {i}: {a}x + {b} = {c}")
        print("-" * 40)
        
        solver = GeneticLinearSolver(a, b, c, pop_size=30, mutation_rate=0.15)
        results = solver.solve(max_generations=200, target_error=1e-6, verbose=False)
        
        print(f"Soluția exactă:    {solver.exact_solution:10.6f}")
        print(f"Soluția găsită:    {results['best_solution']:10.6f}")
        print(f"Eroarea:           {results['error']:10.8f}")
        print(f"Generații:         {results['generations']:10d}")
        print(f"Converged:         {'✅ DA' if results['converged'] else '❌ NU'}")

def interactive_solver():
    """Solver interactiv pentru utilizator."""
    print("\n🎯 SOLVER INTERACTIV")
    print("="*50)
    
    try:
        # Input de la utilizator
        a = float(input("Introduceți coeficientul a: "))
        b = float(input("Introduceți coeficientul b: "))
        c = float(input("Introduceți coeficientul c: "))
        
        print(f"\nEcuația dumneavoastră: {a}x + {b} = {c}")
        
        if a == 0:
            print("❌ Eroare: a nu poate fi 0 pentru o ecuație liniară!")
            return
        
        # Parametrii algoritmului
        print("\n⚙️  Setări algoritm (apăsați Enter pentru valorile implicite):")
        
        pop_size = input("Mărimea populației [50]: ").strip()
        pop_size = int(pop_size) if pop_size else 50
        
        max_gen = input("Numărul maxim de generații [500]: ").strip()
        max_gen = int(max_gen) if max_gen else 500
        
        target_err = input("Eroarea țintă [1e-6]: ").strip()
        target_err = float(target_err) if target_err else 1e-6
        
        # Rulăm algoritmul
        solver = GeneticLinearSolver(a, b, c, pop_size=pop_size)
        results = solver.solve(max_generations=max_gen, target_error=target_err)
        
        # Întrebăm dacă vrea să vadă graficele
        show_plot = input("\nDoriți să vedeți graficele evoluției? (y/n) [n]: ").strip().lower()
        if show_plot == 'y':
            solver.plot_evolution()
            
    except ValueError:
        print("❌ Eroare: Introduceți doar numere valide!")
    except KeyboardInterrupt:
        print("\n⏹️  Oprire la cererea utilizatorului.")

# Exemplu de utilizare principală
if __name__ == "__main__":
    # Rulăm exemple
    run_examples()
    
    # Solver interactiv
    interactive_solver()
    
    # Exemplu detaliat cu grafice
    print("\n📊 EXEMPLU DETALIAT CU GRAFICE")
    print("="*50)
    
    # Ecuația: 5x - 3 = 17  =>  x = 4
    solver = GeneticLinearSolver(a=5, b=-3, c=17, pop_size=100, mutation_rate=0.1)
    results = solver.solve(max_generations=300, target_error=1e-8)
    
    # Afișăm graficele (decomentați dacă aveți matplotlib)
    # solver.plot_evolution(save_plot=True)
