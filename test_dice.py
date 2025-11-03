"""
Tests for dice rolling functionality.
Run with: pytest backend/tests/test_dice.py
"""
import sys
sys.path.insert(0, '../')

from app.services.dice_engine import DiceRoller


def test_simple_d20():
    """Test rolling a simple d20."""
    roller = DiceRoller()
    result = roller.roll("1d20")
    
    assert result["num_dice"] == 1
    assert result["die_size"] == 20
    assert result["modifier"] == 0
    assert 1 <= result["total"] <= 20
    assert len(result["rolls"]) == 1


def test_multiple_dice_with_modifier():
    """Test rolling multiple dice with a modifier."""
    roller = DiceRoller()
    result = roller.roll("2d6+3")
    
    assert result["num_dice"] == 2
    assert result["die_size"] == 6
    assert result["modifier"] == 3
    assert 5 <= result["total"] <= 15  # min: 2+3, max: 12+3
    assert len(result["rolls"]) == 2


def test_negative_modifier():
    """Test rolling with a negative modifier."""
    roller = DiceRoller()
    result = roller.roll("1d20-2")
    
    assert result["modifier"] == -2
    assert result["total"] == result["subtotal"] - 2


def test_invalid_expression():
    """Test that invalid expressions return an error."""
    roller = DiceRoller()
    result = roller.roll("invalid")
    
    assert "error" in result


def test_invalid_die_size():
    """Test that invalid die sizes return an error."""
    roller = DiceRoller()
    result = roller.roll("1d37")  # d37 doesn't exist
    
    assert "error" in result


def test_advantage():
    """Test rolling with advantage."""
    roller = DiceRoller()
    result = roller.roll("1d20", advantage=True)
    
    assert result["num_dice"] == 1
    assert result["die_size"] == 20
    assert "note" in result
    assert "advantage" in result["note"]


def test_roll_history():
    """Test that roll history is maintained."""
    roller = DiceRoller()
    roller.clear_history()
    
    roller.roll("1d20")
    roller.roll("2d6")
    roller.roll("1d8+2")
    
    history = roller.get_history()
    assert len(history) == 3


def test_roll_multiple():
    """Test rolling the same expression multiple times."""
    roller = DiceRoller()
    results = roller.roll_multiple("4d6", times=6)
    
    assert len(results) == 6
    for result in results:
        assert result["num_dice"] == 4
        assert result["die_size"] == 6


if __name__ == "__main__":
    # Run a quick manual test
    roller = DiceRoller()
    
    print("Testing dice roller...")
    print("\n1d20:", roller.roll("1d20"))
    print("\n2d6+3:", roller.roll("2d6+3"))
    print("\n1d20 with advantage:", roller.roll("1d20", advantage=True))
    print("\nRolling stats (4d6, six times):")
    stats = roller.roll_multiple("4d6", times=6)
    for i, stat in enumerate(stats, 1):
        print(f"  Stat {i}: {stat['rolls']} = {stat['total']}")
