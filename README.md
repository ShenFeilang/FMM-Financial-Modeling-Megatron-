## 项目背景

在当代商业和社会背景下，人工智能技术的应用使企业管理更趋向于数据驱动，财务数据管理对企业的重要性愈发凸显， 准确的财务数据是企业把握公司情况，社会发展，做出明智决策的基础。随着人工智能技术的快速发展，机器学习与大语言模型等技术不仅可以通过处理大规模财务数据，挖掘出隐藏的深度信息，还可以根据要求识别数据模式与趋势，为企业提供更深层次与智能化的洞察，助力企业积极应对复杂多变的经济和社会挑战。

项目具体可以解耦成两部分：用于财务分析的大模型研究，面向企业高管的财务分析网站的设计与实现。

用于财务分析的大模型。大模型部分将利用网络爬虫和大数据分析挖掘方法，收集并解析金融领域的相关数据，构建全面而准确的金融知识库。模型将使用搭建而成的数据库进行预训练，并利用SFT技术，将收集到的财务报表数据用于大模型的指令微调，增强模型的思维链能力。基于预训练和微调后的模型，可以实现自动化，智能化的财务报表分析，并可以通过与其他公司的财务情况对标，分析差距，快速了解企业运行优势与不足，并给出相应的调整策略和建议。

面向企业高管的财务分析网站的设计与实现。为了更好地将大模型的分析能力应用于实际场景，本项目将以网页的形式实现该智能财务分析系统。这个网页会作为一个智能工具，帮助企业快速直观地理解和财务情况，并根据模型分析结果展示出智能决策支持。通过大模型的连接，该智能系统可以接收用户输入的财务数据，并将其传递给大模型进行分析。在得到结果后，系统会将结果直观地呈现给用户，并提供详细的解释和建议。企业可以根据这些智能分析结果与建议，更加快速与积极地做出相应调整和决策，以优化企业的运营管理。

# 项目介绍

本项目旨在为企业高管提供财务分析服务。团队具备丰富的技术和行业知识，通过学校和公司的联合培训，确保技术能力和实践经验的卓越水平。目前，项目已成功完成了基础模型的训练。为了确保模型的准确性和可用性，还收集了大量金融语料数据，这些数据将用于模型的进一步训练和优化，使得项目在金融领域的应用更加可靠和精确。项目团队已经积累了充足的CoT数据，这些数据在金融财务分析中具有极高的价值。这些数据将被用于针对金融财务分析的模型微调，以确保模型能够应对复杂的金融情景和变化。