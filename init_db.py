from finance.database import Base, engine
from finance.models import Transaction

print("📦 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")
