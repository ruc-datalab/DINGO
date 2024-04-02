single_score_template = {
    "Code":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The generated code or explanation in the response needs to be correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Code (with reference answer)":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The generated code or explanation in the response needs to be correct. You can compare the AI response with the reference question and answer.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response does not contain any hazardous or harmful information.
                Here are reference question and answer:
                Question: {ref_question}
                Answer: {ref_answer}
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Creation":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The content of the response should be what the user needs.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response need to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Knowledge Utilization":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The answer in the response needs to be factual and correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Language Generation":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The content of the response should be what the user needs.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response need to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Language Understanding":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The answer in the response needs to be factual and correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Mathematics and Reasoning":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The answer needs to be correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and AI:
                {conversation}
            """,
    "Mathematics and Reasoning (with reference answer)":
            """
                Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question. Your evaluation should consider correctness and helpfulness. You evaluation should focus on the AI assistant's answer to the user's question. Be as objective as possible. After providing your explanation, you must rate the response on a scale of 1 to 10 by strictly following this format: \"[[rating]]\", for example: \"Rating: [[5]]\". Here are some important scoring criteria that you need to consider:
                1. The answer needs to be correct. You can compare the AI response with the reference question and answer.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here are reference question and answer:
                Question: {ref_question}
                Answer: {ref_answer}
                Here is the conversation between user and AI:
                {conversation}
            """
}


pairwise_score_template = {
    "Code":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The generated code or explanation in the response needs to be correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Code (with reference answer)":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The generated code or explanation in the response needs to be correct. You can compare the AI response with the reference question and answer.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response does not contain any hazardous or harmful information.
                Here are reference question and answer:
                Question: {ref_question}
                Answer: {ref_answer}
                Here is the conversation between user and two AI assitants:
                {conversation}
            """,
    "Creation":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The content of the response should be what the user needs.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response need to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Knowledge Utilization":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The answer in the response needs to be factual and correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Language Generation":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The content of the response should be what the user needs.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The response needs to be clear and easy to understand, so that user can easily understand.
                4. The response need to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Language Understanding":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The answer in the response needs to be factual and correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, word limit, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Mathematics and Reasoning":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants A and B to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The answer needs to be correct.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here is the conversation between user and two AI assistants:
                {conversation}
            """,
    "Mathematics and Reasoning (with reference answer)":
            """
                Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible. After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie. Here are some important scoring criteria that you need to consider:
                1. The answer needs to be correct. You can compare the AI response with the reference question and answer.
                2. The response needs to meet the fine-grained constraints of user, such as format, language, and style.
                3. The explanation in the response needs to be clear and easy to understand, so that user can easily understand. If the user does not need an explanation, skip this point.
                4. The explanation in the response needs to be logically reasonable, and logical coherence should be maintained between different parts to avoid self contradiction. If the user does not need an explanation, skip this point.
                5. The response does not contain any hazardous or harmful information.
                Here are reference question and answer:
                Question: {ref_question}
                Answer: {ref_answer}
                Here is the conversation between user and two AI assistants:
                {conversation}
            """
}