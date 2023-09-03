from typing import Any, Dict, List, Optional, Sequence, Union
from langchain.schema import AgentAction, BaseMessage, LLMResult, AgentFinish
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema.document import Document

from uuid import UUID


class PrettyPrintCallbackHandler(BaseCallbackHandler):
    """Base callback handler that can be used to handle callbacks from langchain."""

    ### LLLms
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running."""
        #  print(f"on_llm_start -serial {serialized}")

        for prompt in prompts:
            print(f"\n=============\n[llm][start] - prompts: {prompt}")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        """Run on new LLM token. Only available when streaming is enabled."""
        print(f"[llm][new_token] {token}")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running."""
        for generation in response.generations:
            print(f"\n=============\n[llm][end] - generation {generation[0].text}")
        # print(f"on_llm_end {response}")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""

    ### Chat model
    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        **kwargs: Any,
    ) -> Any:
        """Run when Chat Model starts running."""
        #  print(f"on_chat_model_start -serial {serialized}")
        for message in messages:
            for sub in message:
                print(f"[chat_model][start] - prompts : {sub.content}")

    #### Chains
    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""
        # print(f"[chain][start]{serialized}, {inputs}")
        print(f"[chain][start] - inputs {inputs}")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        print(f"[chain][end] - outputs: {outputs}")

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when chain errors."""

    ### Tools
    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        """Run when tool starts running."""
        print(f"[tool][start] - input_str: {input_str}")

    def on_tool_end(self, output: str, **kwargs: Any) -> Any:
        """Run when tool ends running."""
        print(f"[tool][end] - output: {output}")

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when tool errors."""
        print(f"[tool][error] - error: {error}")

    ### Text
    def on_text(self, text: str, **kwargs: Any) -> Any:
        """Run on arbitrary text."""
        print(f"\n=============\n[text] {text}\n==============")

    ### Agent
    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        print(f"[agent][action] - action: {action}")

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        """Run on agent end."""
        print(f"[agent][finish] - finish: {finish}")

    ### Retrievers
    def on_retriever_end(
        self,
        documents: Sequence[Document],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """Run on retriever end."""

    def on_retriever_error(
        self,
        error: Union[Exception, KeyboardInterrupt],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """Run on retriever error."""
