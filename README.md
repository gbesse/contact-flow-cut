# contact-flow-cut

## Français

Montrer le goulot de livraison dans un réseau de contacts spatiaux.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m contact_flow_cut examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Max-flow entier sur graphe déployé dans le temps, avec capacité des contacts et de stockage entre instants. La coupe résiduelle est un certificat vérifiable du goulot. Contrairement à Contact Market, ne choisit pas des contrats ni des antennes.

### Limites

Octets divisibles, contacts fixes, relais instantané au même horodatage ; pas de routage BPv7 natif, paquets indivisibles ou concurrence radio.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Show the delivery bottleneck in a space contact network.

Synthetic data; no network access or secret required.

```sh
python -m contact_flow_cut examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Integer max-flow on a time-expanded graph with contact and inter-time storage capacities. The residual cut certifies the bottleneck. Unlike Contact Market, it does not select contracts or antennas.

### Limits

Divisible bytes, fixed contacts and instantaneous same-time handoff; no native BPv7 routing, indivisible packets or radio contention.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Mostrar el cuello de botella de entrega en una red de contactos espaciales.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m contact_flow_cut examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Flujo máximo entero en grafo temporal con capacidades de contacto y almacenamiento entre instantes. El corte residual certifica el cuello de botella. A diferencia de Contact Market, no selecciona contratos ni antenas.

### Límites

Bytes divisibles, contactos fijos y transferencia instantánea en el mismo instante; sin enrutamiento BPv7 nativo, paquetes indivisibles ni contención radio.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.rfc-editor.org/rfc/rfc9171
