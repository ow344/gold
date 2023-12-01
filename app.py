from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
data = []

# Create operation
@app.route('/items', methods=['POST'])
def create_item():
    item = request.get_json()
    data.append(item)
    return jsonify(item), 201

# Read operation
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(data)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in data:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Update operation
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in data:
        if item['id'] == item_id:
            updated_item = request.get_json()
            item.update(updated_item)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Delete operation
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in data:
        if item['id'] == item_id:
            data.remove(item)
            return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run()
