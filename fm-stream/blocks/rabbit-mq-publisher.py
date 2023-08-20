from gnuradio import gr
import pika


class RabbitMQPublisher(gr.sync_block):
    def __init__(self, exchange_name, routing_key, host='localhost', port=5672):
        gr.sync_block.__init__(self,
            name="RabbitMQ Publisher",
            in_sig=[],
            out_sig=[])

        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='topic')

    def work(self, input_items, output_items):
        # Generate your message content here
        message = "Your message content"

        # Publish the message to RabbitMQ
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message
        )

        return len(input_items[0])
