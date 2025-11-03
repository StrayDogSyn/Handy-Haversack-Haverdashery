"""
Tests for dice rolling service
"""

import pytest
from app.services.dice_service import DiceService


def test_parse_notation_simple():
    """Test parsing simple dice notation"""
    service = DiceService()
    num, size, mod = service.parse_notation("2d6")
    assert num == 2
    assert size == 6
    assert mod == 0


def test_parse_notation_with_modifier():
    """Test parsing notation with modifier"""
    service = DiceService()
    
    # Positive modifier
    num, size, mod = service.parse_notation("2d6+3")
    assert num == 2
    assert size == 6
    assert mod == 3
    
    # Negative modifier
    num, size, mod = service.parse_notation("1d20-1")
    assert num == 1
    assert size == 20
    assert mod == -1


def test_parse_notation_invalid():
    """Test that invalid notation raises ValueError"""
    service = DiceService()
    
    with pytest.raises(ValueError):
        service.parse_notation("invalid")
    
    with pytest.raises(ValueError):
        service.parse_notation("2d7")  # Invalid die size
    
    with pytest.raises(ValueError):
        service.parse_notation("101d6")  # Too many dice


def test_roll_dice():
    """Test dice rolling"""
    service = DiceService()
    result = service.roll_dice("2d6+3")
    
    assert result["notation"] == "2d6+3"
    assert result["num_dice"] == 2
    assert result["die_size"] == 6
    assert result["modifier"] == 3
    assert len(result["rolls"]) == 2
    assert all(1 <= r <= 6 for r in result["rolls"])
    assert result["total"] == sum(result["rolls"]) + 3


def test_roll_with_advantage():
    """Test rolling with advantage"""
    service = DiceService()
    result = service.roll_with_advantage()
    
    assert result["type"] == "advantage"
    assert len(result["rolls"]) == 2
    assert result["result"] == max(result["rolls"])


def test_roll_with_disadvantage():
    """Test rolling with disadvantage"""
    service = DiceService()
    result = service.roll_with_disadvantage()
    
    assert result["type"] == "disadvantage"
    assert len(result["rolls"]) == 2
    assert result["result"] == min(result["rolls"])


def test_roll_history():
    """Test roll history tracking"""
    service = DiceService()
    
    # Clear history first
    service.clear_history()
    assert len(service.get_history()) == 0
    
    # Make some rolls
    service.roll_dice("1d20")
    service.roll_dice("2d6+3")
    
    history = service.get_history()
    assert len(history) == 2
    
    # Clear again
    service.clear_history()
    assert len(service.get_history()) == 0


def test_calculate_average():
    """Test average calculation"""
    avg = DiceService.calculate_average("2d6+3")
    assert avg == 10.0  # (3.5 * 2) + 3
    
    avg = DiceService.calculate_average("1d20")
    assert avg == 10.5


def test_all_dice_types():
    """Test all supported dice types"""
    service = DiceService()
    
    dice_types = [4, 6, 8, 10, 12, 20, 100]
    for die in dice_types:
        result = service.roll_dice(f"1d{die}")
        assert 1 <= result["rolls"][0] <= die
