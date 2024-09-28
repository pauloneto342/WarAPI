from playerbuilder import PlayerBuilder
from objective import Objective


def test_player_builder():
    player_builder = PlayerBuilder("Player")
    player = (player_builder
              .set_color("vermelho")
              .set_army(10)
              .set_objective(Objective("Objective"))
              .build())
    
    assert player.get_name() == "Player"
    assert player.get_color() == "vermelho"
    assert player.get_army() == 10
    assert player.get_objective().get_objective() == "Objective"

def test_objective_completion():
    objective = Objective("Objective")
    objective.set_complete()
    assert objective.is_complete()  

def test_set_army():
    player_builder = PlayerBuilder("Player")
    player = (player_builder
              .set_color("azul")
              .set_army(20)
              .set_objective(Objective("Objective"))
              .build())
    
    assert player.get_army() == 20

def test_set_color():
    player_builder = PlayerBuilder("Player")
    player = (player_builder
              .set_color("verde")
              .set_army(15)
              .set_objective(Objective("Objective"))
              .build())
    
    assert player.get_color() == "verde"

def test_add_multiple_army():
    player_builder = PlayerBuilder("Player")
    player = (player_builder
              .set_color("amarelo")
              .set_army(10)
              .set_objective(Objective("Avançar"))
              .build())

    player.add_army(5)
    assert player.get_army() == 15

def test_change_objective():
    player_builder = PlayerBuilder("Player")
    player = (player_builder
              .set_color("cinza")
              .set_army(5)
              .set_objective(Objective("Objective"))
              .build())
    
    new_objective = Objective("New Objective")
    player.set_objective(new_objective)
    assert player.get_objective().get_objective() == "New Objective"

def test_initial_army_zero():
    player_builder = PlayerBuilder("Player")
    player = (player_builder 
              .set_color("laranja")
              .set_army(0)
              .set_objective(Objective("Objective"))
              .build())
    
    assert player.get_army() == 0

