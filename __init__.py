from .nodes import TraditionalToSimplifiedNode, SimplifiedToTraditionalNode

NODE_CLASS_MAPPINGS = {
	"TraditionalToSimplified": TraditionalToSimplifiedNode,
	"SimplifiedToTraditional": SimplifiedToTraditionalNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
	"TraditionalToSimplified": "Traditional to Simplified Chinese",
	"SimplifiedToTraditional": "Simplified to Traditional Chinese",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']