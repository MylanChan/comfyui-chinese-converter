import opencc
from typing import Tuple

class SimplifiedToTraditionalNode:
	
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"text": (
					"STRING", {
						"multiline": True
					}
				),
			}
		}
	
	RETURN_TYPES = ("STRING",)
	RETURN_NAMES = ("text",)
	FUNCTION = "convert_text"
	
	def __init__(self):
		self.converter = None
	
	def get_converter(self):
		if self.converter is None:
			self.converter = opencc.OpenCC('s2t')
		return self.converter
	
	def convert_text(self, text: str) -> Tuple[str]:
		if not text or not text.strip():
			return ("",)
		
		converter = self.get_converter()
		result = converter.convert(text)
		
		return (result,)
	
	@classmethod
	def IS_CHANGED(cls, text: str) -> float:
		return hash(text)
