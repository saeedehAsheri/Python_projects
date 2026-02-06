from typing import List, Dict, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Management system for organizing matches and leaderboards."""

    def __init__(self) -> None:
        """Initializes an empty registry and match tracker."""
        self._registry: Dict[str, TournamentCard] = {}
        self._total_matches: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Registers a card in the tournament system."""
        self._registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Simulates a match between two cards and updates rankings."""
        c1 = self._registry[card1_id]
        c2 = self._registry[card2_id]

        # Simplified logic: higher rating or random could win.
        # Here, we'll make card1 win for demonstration.
        c1.update_wins(1)
        c2.update_losses(1)
        self._total_matches += 1

        return {
            'winner': c1.card_id,
            'loser': c2.card_id,
            'winner_rating': c1.calculate_rating(),
            'loser_rating': c2.calculate_rating()
        }

    def get_leaderboard(self) -> List[str]:
        """Returns a list of cards sorted by their rating."""
        sorted_cards = sorted(
            self._registry.values(),
            key=lambda x: x.calculate_rating(),
            reverse=True
        )
        leaderboard = []
        for i, card in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            entry = (
                f"{i}. {card.name} - Rating: {info['rating']} "
                f"({info['wins']}-{info['losses']})"
            )
            leaderboard.append(entry)
        return leaderboard

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Generates a summary of the platform status."""
        total_cards = len(self._registry)
        avg_rating = 0
        if total_cards > 0:
            total_r = sum(
                c.calculate_rating() for c in self._registry.values()
                )
            avg_rating = total_r // total_cards

        return {
            'total_cards': total_cards,
            'matches_played': self._total_matches,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
