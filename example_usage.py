from client import SkillWorkflowReuserClient
client = SkillWorkflowReuserClient()
result = client.run_workflow("sales_proposal", {
    "company_name": "Acme Corp",
    "industry": "Healthcare",
    "budget": "$50k",
    "contact_email": "ceo@acme.com"
})
print(f"Workflow found: {result['workflow_found']}")
for step in result["rendered_workflow"]:
    print(f"  {step}")
