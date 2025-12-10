import openai
from chat.chat_llm import ChatLLM
from chat.chat_schema import ChatDTO
from uuid import UUID
from sqlalchemy.orm import Session
from chat.chat_crud import ChatCRUD


class ChatService:
    
    def __init__(self):
        self.chat_crud = ChatCRUD()
        
    
    # 사용자로부터 질문(Query)를 받아 답변을 생성하고 전달하는 기능
    async def gen_answer(self, chat_dto: ChatDTO, session_id:UUID, llm: ChatLLM, db:Session) -> str:
        chat = {
            "session_id": str(session_id),
            "msg_type": "Human",
            "message": chat_dto.query,
        }
        
        # self.chat_crud.save_chat(chat, db)
        
        # AI Answer 생성
        answer = llm.multiturn_chat(chat_dto.query, session_id)
        
        # AI Answer를 DB 저장!
        chat = {
            "session_id": str(session_id),
            "msg_type": "AI",
            "message": answer,
        }
        # self.chat_crud.save_chat(chat, db)
        
        return answer