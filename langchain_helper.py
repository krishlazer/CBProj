from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
# from ds_langchain_placesofinterest_app1 import currency_chain
import os

openai_api_key = os.environ.get("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7)
def generate_currency_and_places_of_interest(country):
    prompt_template_places = PromptTemplate(
        input_variables=['country'],
        template="What is the currency in {country}?"
    )
    places_of_interest_chain = LLMChain(llm=llm, prompt=prompt_template_places, output_key="places_of_interest")

    chain = SequentialChain(
        chains=[currency_chain, places_of_interest_chain], input_variables=['country'],
        output_variables=['currency', 'places_of_interest'])

    response = chain({"country": country})

