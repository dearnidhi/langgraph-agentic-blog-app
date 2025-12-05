from src.states.blogstate import BlogState

class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            prompt = """
                 You are an expert blog content writer. Use Markdown formatting.
                 Generate a blog title for the {topic}. The title must be creative and SEO friendly.
            """
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            # Update state
            return {"blog":{"title": response.content}}

    def content_generation(self, state: BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """
                 You are an expert blog content writer. Use Markdown formatting.
                 Generate detailed blog content for the {topic}.
            """
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            # Update existing state
            state['blog']['content'] = response.content
            return state
