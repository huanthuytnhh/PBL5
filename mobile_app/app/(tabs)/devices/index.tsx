import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Modal } from 'react-native';
import { Lightbulb, Fan, Tv, Lock, Power, Wifi, Mic, Plus, Trash2 } from 'lucide-react-native';
import { useState, useEffect } from 'react';
import { useRouter } from 'expo-router';

const devices = [
  { id: 1, name: 'Living Room Light', icon: Lightbulb, isOn: true, type: 'Light', room: 'Living Room', lastUsed: '2 hours ago' },
  { id: 2, name: 'AC Unit', icon: Fan, isOn: false, type: 'Climate', room: 'Bedroom', lastUsed: '1 day ago' },
  { id: 3, name: 'Smart TV', icon: Tv, isOn: true, type: 'Entertainment', room: 'Living Room', lastUsed: '30 mins ago' },
  { id: 4, name: 'Front Door Lock', icon: Lock, isOn: true, type: 'Security', room: 'Entrance', lastUsed: '5 mins ago' },
  { id: 5, name: 'WiFi Router', icon: Wifi, isOn: true, type: 'Network', room: 'Office', lastUsed: 'Just now' },
];

export default function DevicesScreen() {
  const [isListening, setIsListening] = useState(false);
  const [selectedDevice, setSelectedDevice] = useState(null);
  const [showOptions, setShowOptions] = useState(false);
  const router = useRouter();

  useEffect(() => {
    let timeoutId;
    if (isListening) {
      timeoutId = setTimeout(() => {
        setIsListening(false);
      }, 2000);
    }
    return () => {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
    };
  }, [isListening]);

  const handleVoiceCommand = () => {
    setIsListening(true);
  };

  const handleDevicePress = (device) => {
    router.push(`/devices/details?id=${device.id}`);
  };

  const handleAddDevice = () => {
    router.push('/devices/add');
  };

  return (
    <View style={styles.container}>
      <ScrollView>
        <View style={styles.header}>
          <Text style={styles.title}>My Devices</Text>
          <TouchableOpacity style={styles.addButton} onPress={handleAddDevice}>
            <Plus size={20} color="#ffffff" />
            <Text style={styles.addButtonText}>Add Device</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.deviceGrid}>
          {devices.map((device) => {
            const DeviceIcon = device.icon;
            return (
              <TouchableOpacity
                key={device.id}
                style={styles.deviceCard}
                onPress={() => handleDevicePress(device)}
                onLongPress={() => {
                  setSelectedDevice(device);
                  setShowOptions(true);
                }}>
                <View style={[styles.iconContainer, device.isOn && styles.iconContainerActive]}>
                  <DeviceIcon size={24} color={device.isOn ? '#ffffff' : '#8E8E93'} />
                </View>
                <Text style={styles.deviceName}>{device.name}</Text>
                <Text style={styles.deviceType}>{device.type}</Text>
                <Text style={styles.lastUsed}>{device.lastUsed}</Text>
                <TouchableOpacity 
                  style={[styles.powerButton, device.isOn && styles.powerButtonActive]}
                >
                  <Power size={16} color={device.isOn ? '#ffffff' : '#8E8E93'} />
                </TouchableOpacity>
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>

      <TouchableOpacity
        style={[styles.voiceButton, isListening && styles.voiceButtonActive]}
        onPress={handleVoiceCommand}>
        <Mic size={24} color="#ffffff" />
      </TouchableOpacity>

      <Modal
        visible={showOptions}
        transparent
        animationType="fade"
        onRequestClose={() => setShowOptions(false)}>
        <TouchableOpacity
          style={styles.modalOverlay}
          activeOpacity={1}
          onPress={() => setShowOptions(false)}>
          <View style={styles.modalContent}>
            <TouchableOpacity style={styles.modalOption}>
              <Text style={styles.modalOptionText}>Edit Device</Text>
            </TouchableOpacity>
            <TouchableOpacity style={[styles.modalOption, styles.deleteOption]}>
              <Text style={styles.deleteText}>Delete Device</Text>
            </TouchableOpacity>
          </View>
        </TouchableOpacity>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F2F2F7',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#ffffff',
  },
  title: {
    fontSize: 28,
    fontWeight: '700',
    color: '#000000',
  },
  addButton: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  addButtonText: {
    color: '#ffffff',
    fontWeight: '600',
  },
  deviceGrid: {
    padding: 20,
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  deviceCard: {
    backgroundColor: '#ffffff',
    borderRadius: 16,
    padding: 16,
    marginBottom: 20,
    width: '48%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#F2F2F7',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
  },
  iconContainerActive: {
    backgroundColor: '#007AFF',
  },
  deviceName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#000000',
    marginBottom: 4,
  },
  deviceType: {
    fontSize: 14,
    color: '#8E8E93',
    marginBottom: 4,
  },
  lastUsed: {
    fontSize: 12,
    color: '#8E8E93',
    fontStyle: 'italic',
  },
  powerButton: {
    position: 'absolute',
    top: 16,
    right: 16,
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#F2F2F7',
    justifyContent: 'center',
    alignItems: 'center',
  },
  powerButtonActive: {
    backgroundColor: '#007AFF',
  },
  voiceButton: {
    position: 'absolute',
    bottom: 30,
    right: 30,
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 5,
  },
  voiceButtonActive: {
    backgroundColor: '#FF3B30',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: '#ffffff',
    borderRadius: 16,
    padding: 8,
    width: '80%',
    maxWidth: 300,
  },
  modalOption: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#F2F2F7',
  },
  modalOptionText: {
    fontSize: 16,
    color: '#007AFF',
  },
  deleteOption: {
    borderBottomWidth: 0,
  },
  deleteText: {
    fontSize: 16,
    color: '#FF3B30',
  },
});