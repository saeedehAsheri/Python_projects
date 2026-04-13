import json
import math
from pathlib import Path
from typing import Any
from src.errors import ModelError

try:
    from llm_sdk.llm_sdk import Small_LLM_Model
except ImportError as exc:
    raise ModelError(
        "Could not import Small_LLM_Model from llm_sdk. "
        "Make sure the llm_sdk directory is present at the project root."
    ) from exc

class LLMInterface:
    """A class for using the provided llm_sdk"""
    def __init__(self):
        try:
            self.model = Small_LLM_Model()
        except Exception as exc:
            raise ModelError(
                f"Failed to initialize the model: {exc}") from exc


    def get_tokenizer_metadata_path(self)-> str:
        """Return tokenizer metadata path from the SDK."""
        try:
            return self.model.get_path_to_tokenizer_file()
        except Exception as exc:
            raise ModelError(f"Failed to get tokenizer file path: {exc}") from exc
        
    def load_tokenizer_metadata(self)-> dict[str, Any]:
        """Load tokenizer metadata JSON when available"""
        tokenizer_path = Path(self.get_tokenizer_metadata_path())
        if not tokenizer_path.exists():
            return {}
        
        try:
            with open(tokenizer_path, "r", encoding= "utf-8") as file:
                return json.load(file)
        except Exception:
            return {}
    
    def compute_log_prob(self, prompt: str, continuation: str)-> float:
        """Compute a log-prob-like score for a continuation given a prompt."""
        try:
            prompt_tensor = self.model.encode(prompt)
            full_tensor = self.model.encode(prompt + continuation)
        except Exception as exc:
            raise ModelError(f"Encoding failed: {exc}") from exc
        
        prompt_ids = prompt_tensor[0].tolist()
        full_ids = full_tensor[0].tolist()

        if len(full_ids) <= len(prompt_ids):
            return float("-inf")
    
        continuation_ids = full_ids[len(prompt_ids):]
        running_ids = list(prompt_ids)
        total_logprob = 0.0

        for token_id in continuation_ids:
            try:
                logits = self.model.get_logits_from_input_ids(running_ids)
            except Exception as exc:
                raise ModelError(f"Failed to obtain logits: {exc}") from exc

            max_logit = max(logits)
            exp_sum = 0.0
            for logit in logits:
                exp_sum += math.exp(logit - max_logit)

            token_logprob = (
                logits[token_id]
                - max_logit
                - math.log(exp_sum)
            )
            total_logprob += token_logprob
            running_ids.append(token_id)

        return total_logprob